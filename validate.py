from pathlib import Path
import sys

import yaml


FILES = {
    "base": Path("schemas/metarci-base.yaml"),
    "profile": Path("profiles/example-profile.yaml"),
    "record": Path("examples/example-record.yaml"),
}


def load_yaml(path: Path) -> dict:
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

    if "metarci" not in base:
        print("ERROR: Base schema is missing the 'metarci' root.")
        return 1

    if "metarci_profile" not in profile:
        print("ERROR: Example profile is missing the 'metarci_profile' root.")
        return 1

    if "metarci_record" not in record:
        print("ERROR: Example record is missing the 'metarci_record' root.")
        return 1

    required_tiers = {"reference", "context", "interpretive"}

    base_tiers = set(
        base["metarci"].get("tiers", {}).keys()
    )

    record_tiers = set(
        record["metarci_record"].keys()
    )

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

    reference_record = record["metarci_record"].get("reference", {})

    required_reference_fields = {
        field_name
        for field_name, field_definition in (
            base["metarci"]["tiers"]["reference"]
            .get("fields", {})
            .items()
        )
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

    print("OK: All YAML files parsed successfully.")
    print("OK: Expected MetaRCI roots are present.")
    print("OK: Reference, Context, and Interpretive tiers are present.")
    print("OK: Required Reference fields are present.")

    return 0


if __name__ == "__main__":
    sys.exit(main())