from pathlib import Path
import sys

import yaml


FILES = {
    "base": Path("schemas/metarci-base.yaml"),
    "profile": Path("profiles/example-profile.yaml"),
    "record": Path("examples/example-record.yaml"),
}


def load_yaml(path: Path) -> dict:
    """Load one YAML file and confirm its root is a mapping."""
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML mapping in {path}")

    return data


def main() -> int:
    try:
        documents = {
            name: load_yaml(path)
            for name, path in FILES.items()
        }
    except (FileNotFoundError, ValueError, yaml.YAMLError) as error:
        print(f"ERROR: {error}")
        return 1

    base = documents["base"]
    profile = documents["profile"]
    record = documents["record"]

    # Confirm the expected root keys exist.
    if "metarci" not in base:
        print("ERROR: Base schema is missing the 'metarci' root.")
        return 1

    if "metarci_profile" not in profile:
        print("ERROR: Example profile is missing the 'metarci_profile' root.")
        return 1

    if "metarci_record" not in record:
        print("ERROR: Example record is missing the 'metarci_record' root.")
        return 1

    base_data = base["metarci"]
    profile_data = profile["metarci_profile"]
    record_data = record["metarci_record"]

    # Confirm that the record uses the declared profile version.
    declared_profile_version = profile_data.get("version")
    record_profile_version = record_data.get("profile_version")

    if declared_profile_version != record_profile_version:
        print(
            "ERROR: Record profile_version does not match "
            f"the profile version. Expected '{declared_profile_version}', "
            f"got '{record_profile_version}'."
        )
        return 1

    # Confirm that all three MetaRCI tiers exist.
    required_tiers = {"reference", "context", "interpretive"}

    base_tiers = set(
        base_data.get("tiers", {}).keys()
    )

    record_tiers = {
        tier_name
        for tier_name in record_data.keys()
        if tier_name in required_tiers
    }

    missing_base_tiers = required_tiers - base_tiers
    missing_record_tiers = required_tiers - record_tiers

    if missing_base_tiers:
        print(
            "ERROR: Base schema is missing tiers: "
            + ", ".join(sorted(missing_base_tiers))
        )
        return 1

    if missing_record_tiers:
        print(
            "ERROR: Example record is missing tiers: "
            + ", ".join(sorted(missing_record_tiers))
        )
        return 1

    # Read the Tier 1 schema and record values.
    reference_schema = (
        base_data["tiers"]["reference"]
        .get("fields", {})
    )

    reference_record = record_data.get("reference", {})

    # Confirm that all required Tier 1 fields exist and are not null.
    required_reference_fields = {
        field_name
        for field_name, field_definition in reference_schema.items()
        if field_definition.get("requirement") == "required"
    }

    missing_required_fields = {
        field_name
        for field_name in required_reference_fields
        if field_name not in reference_record
        or reference_record[field_name] is None
    }

    if missing_required_fields:
        print(
            "ERROR: Example record is missing required Reference fields: "
            + ", ".join(sorted(missing_required_fields))
        )
        return 1

    # Confirm extraction_status uses an allowed value.
    extraction_status_schema = reference_schema.get(
        "extraction_status",
        {},
    )

    allowed_statuses = extraction_status_schema.get(
        "allowed_values",
        [],
    )

    extraction_status = reference_record.get("extraction_status")

    if allowed_statuses and extraction_status not in allowed_statuses:
        print(
            "ERROR: Invalid extraction_status "
            f"'{extraction_status}'. Allowed values: "
            + ", ".join(allowed_statuses)
        )
        return 1

    # Confirm every record field is declared in the base schema
    # or added through the active profile.
    custom_fields = profile_data.get("custom_fields", {})

    for tier_name in sorted(required_tiers):
        base_fields = (
            base_data["tiers"][tier_name]
            .get("fields", {})
        )

        profile_fields = custom_fields.get(tier_name, {})

        allowed_fields = set(base_fields) | set(profile_fields)

        record_fields = set(
            record_data.get(tier_name, {}).keys()
        )

        unknown_fields = record_fields - allowed_fields

        if unknown_fields:
            print(
                f"ERROR: Unknown fields in {tier_name} tier: "
                + ", ".join(sorted(unknown_fields))
            )
            return 1

    print("OK: All YAML files parsed successfully.")
    print("OK: Expected MetaRCI roots are present.")
    print("OK: Record profile version matches the profile.")
    print("OK: Reference, Context, and Interpretive tiers are present.")
    print("OK: Required Reference fields are present.")
    print("OK: extraction_status is valid.")
    print("OK: Record fields are declared by the base schema or profile.")

    return 0


if __name__ == "__main__":
    sys.exit(main())