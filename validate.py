from datetime import date, datetime
from pathlib import Path
import sys

import yaml


FILES = {
    "base": Path("schemas/metarci-base.yaml"),
    "profile": Path("profiles/example-profile.yaml"),
    "record": Path("examples/example-record.yaml"),
}

REQUIRED_TIERS = {
    "reference",
    "context",
    "interpretive",
}

VALID_TYPES = {
    "string",
    "integer",
    "list",
    "object",
    "date",
    "datetime",
}

VALID_REQUIREMENTS = {
    "required",
    "recommended",
    "conditional",
    "optional",
}

VALID_FIELD_ATTRIBUTES = {
    "type",
    "requirement",
    "nullable",
    "description",
    "allowed_values",
    "item_type",
    "properties",
    "item_properties",
}

VALID_PROFILE_ATTRIBUTES = {
    "name",
    "version",
    "status",
    "extends",
    "description",
    "implementation",
    "tier_overrides",
    "custom_fields",
}

REQUIRED_PROFILE_ATTRIBUTES = {
    "name",
    "version",
    "status",
    "extends",
}

VALID_PROFILE_STATUSES = {
    "draft",
    "active",
    "deprecated",
    "retired",
}

VALID_IMPLEMENTATION_ATTRIBUTES = {
    "domain",
    "corpus",
    "use_case",
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


def is_valid_date(value: object) -> bool:
    """Accept a parsed YAML date or an ISO 8601 date string."""
    if isinstance(value, datetime):
        return False

    if isinstance(value, date):
        return True

    if isinstance(value, str):
        try:
            date.fromisoformat(value)
            return True
        except ValueError:
            return False

    return False


def is_valid_datetime(value: object) -> bool:
    """Accept a parsed YAML datetime or an ISO 8601 datetime string."""
    if isinstance(value, datetime):
        return True

    if isinstance(value, str):
        try:
            datetime.fromisoformat(value)
            return True
        except ValueError:
            return False

    return False


def value_matches_type(value: object, declared_type: str) -> bool:
    """Compare a value with a MetaRCI field type."""
    if declared_type == "string":
        return isinstance(value, str)

    if declared_type == "integer":
        # bool is a subclass of int, so reject booleans explicitly.
        return isinstance(value, int) and not isinstance(value, bool)

    if declared_type == "list":
        return isinstance(value, list)

    if declared_type == "object":
        return isinstance(value, dict)

    if declared_type == "date":
        return is_valid_date(value)

    if declared_type == "datetime":
        return is_valid_datetime(value)

    return False


def validate_allowed_values(
    path_name: str,
    value: object,
    definition: dict,
) -> str | None:
    """Validate a value against allowed_values when declared."""
    allowed_values = definition.get("allowed_values")

    if allowed_values is None:
        return None

    if not isinstance(allowed_values, list):
        return (
            f"Schema definition for '{path_name}' declares "
            "allowed_values, but allowed_values is not a list."
        )

    if value not in allowed_values:
        allowed_display = ", ".join(
            repr(allowed_value)
            for allowed_value in allowed_values
        )

        return (
            f"Value for '{path_name}' must be one of: "
            f"{allowed_display}. Received {value!r}."
        )

    return None


def validate_profile_document(
    profile_data: dict,
    profile_path: Path,
    expected_base_path: Path,
) -> str | None:
    """
    Validate the profile's own top-level structure.

    This happens before the profile is used to modify or extend
    the base schema.
    """
    if not isinstance(profile_data, dict):
        return "The metarci_profile value must be a mapping."

    # Reject misspelled or unsupported top-level profile keys.
    unknown_attributes = (
        set(profile_data)
        - VALID_PROFILE_ATTRIBUTES
    )

    if unknown_attributes:
        return (
            "Unknown profile attributes: "
            + ", ".join(sorted(unknown_attributes))
        )

    # Confirm all required profile metadata is present.
    missing_attributes = (
        REQUIRED_PROFILE_ATTRIBUTES
        - set(profile_data)
    )

    if missing_attributes:
        return (
            "Profile is missing required attributes: "
            + ", ".join(sorted(missing_attributes))
        )

    # Required profile metadata must contain non-empty strings.
    for attribute_name in sorted(REQUIRED_PROFILE_ATTRIBUTES):
        attribute_value = profile_data.get(attribute_name)

        if not isinstance(attribute_value, str):
            return (
                f"Profile attribute '{attribute_name}' "
                "must be a string."
            )

        if not attribute_value.strip():
            return (
                f"Profile attribute '{attribute_name}' "
                "cannot be empty."
            )

    # Status is a controlled value.
    status = profile_data["status"]

    if status not in VALID_PROFILE_STATUSES:
        allowed_display = ", ".join(
            sorted(VALID_PROFILE_STATUSES)
        )

        return (
            f"Profile status must be one of: {allowed_display}. "
            f"Received {status!r}."
        )

    # Description is optional, but must be a string when present.
    description = profile_data.get("description")

    if description is not None and not isinstance(description, str):
        return "Profile description must be a string."

    # Confirm that the profile's extends path resolves to the
    # same base schema loaded by this validator.
    extends_value = profile_data["extends"]

    declared_base_path = (
        profile_path.parent / extends_value
    ).resolve()

    loaded_base_path = expected_base_path.resolve()

    if declared_base_path != loaded_base_path:
        return (
            "Profile extends path does not match the base schema "
            f"loaded by the validator. Profile resolves to "
            f"'{declared_base_path}', but validator loaded "
            f"'{loaded_base_path}'."
        )

    # Validate the implementation descriptor.
    implementation = profile_data.get("implementation", {})

    if not isinstance(implementation, dict):
        return "Profile implementation must be a mapping."

    unknown_implementation_attributes = (
        set(implementation)
        - VALID_IMPLEMENTATION_ATTRIBUTES
    )

    if unknown_implementation_attributes:
        return (
            "Unknown implementation attributes: "
            + ", ".join(
                sorted(unknown_implementation_attributes)
            )
        )

    # Each implementation value may be a string or null.
    for attribute_name, attribute_value in implementation.items():
        if attribute_value is not None and not isinstance(
            attribute_value,
            str,
        ):
            return (
                f"Profile implementation.{attribute_name} "
                "must be a string or null."
            )

    # These sections are optional, but must be mappings when present.
    tier_overrides = profile_data.get("tier_overrides", {})

    if not isinstance(tier_overrides, dict):
        return "Profile tier_overrides must be a mapping."

    custom_fields = profile_data.get("custom_fields", {})

    if not isinstance(custom_fields, dict):
        return "Profile custom_fields must be a mapping."

    return None


def validate_property_definitions(
    path_name: str,
    property_definitions: object,
) -> str | None:
    """Validate schema definitions for nested object properties."""
    if not isinstance(property_definitions, dict):
        return (
            f"Schema properties for '{path_name}' "
            "must be a mapping."
        )

    for property_name, property_definition in property_definitions.items():
        error = validate_field_definition(
            f"{path_name}.{property_name}",
            property_definition,
        )

        if error:
            return error

    return None


def validate_field_definition(
    path_name: str,
    field_definition: object,
) -> str | None:
    """Validate one base or custom field definition."""
    if not isinstance(field_definition, dict):
        return (
            f"Schema definition for '{path_name}' "
            "must be a mapping."
        )

    unknown_attributes = (
        set(field_definition)
        - VALID_FIELD_ATTRIBUTES
    )

    if unknown_attributes:
        return (
            f"Unknown schema attributes for '{path_name}': "
            + ", ".join(sorted(unknown_attributes))
        )

    declared_type = field_definition.get("type")

    if declared_type not in VALID_TYPES:
        return (
            f"Schema field '{path_name}' must declare one of "
            f"{sorted(VALID_TYPES)} as its type. "
            f"Received {declared_type!r}."
        )

    requirement = field_definition.get("requirement")

    if requirement not in VALID_REQUIREMENTS:
        return (
            f"Schema field '{path_name}' must declare one of "
            f"{sorted(VALID_REQUIREMENTS)} as its requirement. "
            f"Received {requirement!r}."
        )

    nullable = field_definition.get("nullable")

    if not isinstance(nullable, bool):
        return (
            f"Schema field '{path_name}' must declare nullable "
            "as true or false."
        )

    description = field_definition.get("description")

    if description is not None and not isinstance(description, str):
        return (
            f"Schema field '{path_name}' has a description "
            "that is not a string."
        )

    allowed_values = field_definition.get("allowed_values")

    if allowed_values is not None and not isinstance(
        allowed_values,
        list,
    ):
        return (
            f"Schema field '{path_name}' declares allowed_values, "
            "but allowed_values is not a list."
        )

    if declared_type == "list":
        item_type = field_definition.get("item_type")

        if item_type not in VALID_TYPES:
            return (
                f"List field '{path_name}' must declare a valid "
                f"item_type. Received {item_type!r}."
            )

        item_properties = field_definition.get("item_properties")

        if item_type == "object":
            if item_properties is None:
                return (
                    f"Object-list field '{path_name}' must declare "
                    "item_properties."
                )

            error = validate_property_definitions(
                f"{path_name}[]",
                item_properties,
            )

            if error:
                return error

        elif item_properties is not None:
            return (
                f"List field '{path_name}' declares item_properties, "
                "but its item_type is not 'object'."
            )

    elif "item_type" in field_definition:
        return (
            f"Non-list field '{path_name}' cannot declare item_type."
        )

    elif "item_properties" in field_definition:
        return (
            f"Non-list field '{path_name}' cannot declare "
            "item_properties."
        )

    if declared_type == "object":
        properties = field_definition.get("properties")

        if properties is not None:
            error = validate_property_definitions(
                path_name,
                properties,
            )

            if error:
                return error

    elif "properties" in field_definition:
        return (
            f"Non-object field '{path_name}' cannot declare properties."
        )

    return None


def validate_schema_definitions(
    base_data: dict,
    profile_data: dict,
) -> str | None:
    """
    Validate base fields, custom profile fields, and profile overrides.

    The profile document itself has already been validated before
    this function runs.
    """
    for tier_name in sorted(REQUIRED_TIERS):
        tier_definition = base_data["tiers"].get(tier_name)

        if not isinstance(tier_definition, dict):
            return (
                f"Base tier '{tier_name}' must be a mapping."
            )

        fields = tier_definition.get("fields")

        if not isinstance(fields, dict):
            return (
                f"Base tier '{tier_name}' must declare a fields mapping."
            )

        for field_name, field_definition in fields.items():
            error = validate_field_definition(
                f"{tier_name}.{field_name}",
                field_definition,
            )

            if error:
                return error

    custom_fields = profile_data.get("custom_fields", {})

    unknown_custom_tiers = (
        set(custom_fields)
        - REQUIRED_TIERS
    )

    if unknown_custom_tiers:
        return (
            "Unknown custom-field tiers: "
            + ", ".join(sorted(unknown_custom_tiers))
        )

    for tier_name in sorted(REQUIRED_TIERS):
        tier_custom_fields = custom_fields.get(tier_name, {})

        if not isinstance(tier_custom_fields, dict):
            return (
                f"Profile custom_fields.{tier_name} "
                "must be a mapping."
            )

        for field_name, field_definition in tier_custom_fields.items():
            error = validate_field_definition(
                f"{tier_name}.{field_name}",
                field_definition,
            )

            if error:
                return error

    tier_overrides = profile_data.get("tier_overrides", {})

    unknown_override_tiers = (
        set(tier_overrides)
        - REQUIRED_TIERS
    )

    if unknown_override_tiers:
        return (
            "Unknown override tiers: "
            + ", ".join(sorted(unknown_override_tiers))
        )

    for tier_name, overrides in tier_overrides.items():
        if not isinstance(overrides, dict):
            return (
                f"Profile tier_overrides.{tier_name} "
                "must be a mapping."
            )

        base_fields = (
            base_data["tiers"][tier_name]
            .get("fields", {})
        )

        unknown_override_fields = (
            set(overrides)
            - set(base_fields)
        )

        if unknown_override_fields:
            return (
                f"Unknown field overrides in {tier_name} tier: "
                + ", ".join(sorted(unknown_override_fields))
            )

        for field_name, override_definition in overrides.items():
            override_path = f"{tier_name}.{field_name}"

            if not isinstance(override_definition, dict):
                return (
                    f"Override for '{override_path}' "
                    "must be a mapping."
                )

            unknown_override_attributes = (
                set(override_definition)
                - VALID_FIELD_ATTRIBUTES
            )

            if unknown_override_attributes:
                return (
                    f"Unknown override attributes for "
                    f"'{override_path}': "
                    + ", ".join(sorted(unknown_override_attributes))
                )

            if "type" in override_definition:
                override_type = override_definition["type"]

                if override_type not in VALID_TYPES:
                    return (
                        f"Override for '{override_path}' declares "
                        f"invalid type {override_type!r}."
                    )

            if "requirement" in override_definition:
                override_requirement = (
                    override_definition["requirement"]
                )

                if override_requirement not in VALID_REQUIREMENTS:
                    return (
                        f"Override for '{override_path}' declares "
                        "invalid requirement "
                        f"{override_requirement!r}."
                    )

            if "nullable" in override_definition:
                if not isinstance(
                    override_definition["nullable"],
                    bool,
                ):
                    return (
                        f"Override for '{override_path}' must declare "
                        "nullable as true or false."
                    )

            if "allowed_values" in override_definition:
                if not isinstance(
                    override_definition["allowed_values"],
                    list,
                ):
                    return (
                        f"Override for '{override_path}' declares "
                        "allowed_values that is not a list."
                    )

    return None


def resolve_field_definitions(
    base_data: dict,
    profile_data: dict,
    tier_name: str,
) -> dict:
    """
    Combine base fields, profile overrides, and custom profile fields.

    Overrides modify existing base-field definitions.
    Custom fields add new fields to the resolved tier schema.
    """
    base_fields = (
        base_data["tiers"][tier_name]
        .get("fields", {})
    )

    tier_overrides = (
        profile_data.get("tier_overrides", {})
        .get(tier_name, {})
    )

    custom_fields = (
        profile_data.get("custom_fields", {})
        .get(tier_name, {})
    )

    resolved_fields = {}

    for field_name, field_definition in base_fields.items():
        resolved_definition = dict(field_definition)

        if field_name in tier_overrides:
            resolved_definition.update(
                tier_overrides[field_name]
            )

        resolved_fields[field_name] = resolved_definition

    resolved_fields.update(custom_fields)

    return resolved_fields


def validate_object_against_properties(
    path_name: str,
    value: dict,
    property_definitions: dict,
) -> str | None:
    """Validate one object against its declared property definitions."""
    unknown_properties = set(value) - set(property_definitions)

    if unknown_properties:
        return (
            f"Unknown properties in '{path_name}': "
            + ", ".join(sorted(unknown_properties))
        )

    required_properties = {
        property_name
        for property_name, property_definition
        in property_definitions.items()
        if property_definition.get("requirement") == "required"
    }

    missing_required_properties = {
        property_name
        for property_name in required_properties
        if property_name not in value
        or value[property_name] is None
    }

    if missing_required_properties:
        return (
            f"Missing required properties in '{path_name}': "
            + ", ".join(sorted(missing_required_properties))
        )

    for property_name, property_value in value.items():
        property_definition = property_definitions[property_name]
        property_path = f"{path_name}.{property_name}"
        nullable = property_definition["nullable"]

        if property_value is None:
            if not nullable:
                return (
                    f"Property '{property_path}' "
                    "is null but is not nullable."
                )

            continue

        declared_type = property_definition["type"]

        if not value_matches_type(property_value, declared_type):
            return (
                f"Property '{property_path}' "
                f"must be type '{declared_type}', but received "
                f"'{type(property_value).__name__}'."
            )

        allowed_values_error = validate_allowed_values(
            property_path,
            property_value,
            property_definition,
        )

        if allowed_values_error:
            return allowed_values_error

        if declared_type == "list":
            item_type = property_definition["item_type"]

            for index, item in enumerate(property_value):
                if not value_matches_type(item, item_type):
                    return (
                        f"Item {index} in '{property_path}' "
                        f"must be type '{item_type}', but received "
                        f"'{type(item).__name__}'."
                    )

    return None


def validate_list_items(
    tier_name: str,
    field_name: str,
    value: list,
    field_definition: dict,
) -> str | None:
    """Validate every item in a list field."""
    item_type = field_definition["item_type"]
    item_properties = field_definition.get("item_properties", {})

    for index, item in enumerate(value):
        if not value_matches_type(item, item_type):
            return (
                f"Item {index} in '{tier_name}.{field_name}' "
                f"must be type '{item_type}', but received "
                f"'{type(item).__name__}'."
            )

        if item_type == "object":
            error = validate_object_against_properties(
                f"{tier_name}.{field_name}[{index}]",
                item,
                item_properties,
            )

            if error:
                return error

    return None


def validate_object_properties(
    tier_name: str,
    field_name: str,
    value: dict,
    field_definition: dict,
) -> str | None:
    """Validate nested properties declared for an object field."""
    property_definitions = field_definition.get("properties", {})

    if not property_definitions:
        return None

    return validate_object_against_properties(
        f"{tier_name}.{field_name}",
        value,
        property_definitions,
    )


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

    # Confirm all three tiers exist in the base schema and record.
    base_tiers = set(base_data.get("tiers", {}))

    record_tiers = {
        tier_name
        for tier_name in record_data
        if tier_name in REQUIRED_TIERS
    }

    missing_base_tiers = REQUIRED_TIERS - base_tiers
    missing_record_tiers = REQUIRED_TIERS - record_tiers

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

    # Validate the profile document before using its instructions.
    profile_error = validate_profile_document(
        profile_data,
        FILES["profile"],
        FILES["base"],
    )

    if profile_error:
        print(f"ERROR: {profile_error}")
        return 1

    # Validate the base schema and profile field definitions.
    schema_error = validate_schema_definitions(
        base_data,
        profile_data,
    )

    if schema_error:
        print(f"ERROR: {schema_error}")
        return 1

    # Confirm that the record uses the declared profile version.
    declared_profile_version = profile_data["version"]
    record_profile_version = record_data.get("profile_version")

    if declared_profile_version != record_profile_version:
        print(
            "ERROR: Record profile_version does not match "
            f"the profile version. Expected '{declared_profile_version}', "
            f"got '{record_profile_version}'."
        )
        return 1

    # Resolve base fields, overrides, and custom profile fields.
    resolved_schemas = {
        tier_name: resolve_field_definitions(
            base_data,
            profile_data,
            tier_name,
        )
        for tier_name in REQUIRED_TIERS
    }

    # Confirm required fields across all resolved tiers.
    for tier_name in sorted(REQUIRED_TIERS):
        tier_schema = resolved_schemas[tier_name]
        tier_record = record_data.get(tier_name, {})

        required_fields = {
            field_name
            for field_name, field_definition in tier_schema.items()
            if field_definition.get("requirement") == "required"
        }

        missing_required_fields = {
            field_name
            for field_name in required_fields
            if field_name not in tier_record
            or tier_record[field_name] is None
        }

        if missing_required_fields:
            print(
                f"ERROR: Missing required fields in {tier_name} tier: "
                + ", ".join(sorted(missing_required_fields))
            )
            return 1

    # Confirm each record field exists in the resolved schema.
    for tier_name in sorted(REQUIRED_TIERS):
        allowed_fields = set(resolved_schemas[tier_name])
        record_fields = set(record_data.get(tier_name, {}))

        unknown_fields = record_fields - allowed_fields

        if unknown_fields:
            print(
                f"ERROR: Unknown fields in {tier_name} tier: "
                + ", ".join(sorted(unknown_fields))
            )
            return 1

    # Validate record values against the resolved schema.
    for tier_name in sorted(REQUIRED_TIERS):
        field_definitions = resolved_schemas[tier_name]
        tier_record = record_data.get(tier_name, {})

        for field_name, value in tier_record.items():
            field_definition = field_definitions[field_name]
            field_path = f"{tier_name}.{field_name}"
            nullable = field_definition["nullable"]

            if value is None:
                if not nullable:
                    print(
                        f"ERROR: Field '{field_path}' "
                        "is null but is not nullable."
                    )
                    return 1

                continue

            declared_type = field_definition["type"]

            if not value_matches_type(value, declared_type):
                print(
                    f"ERROR: Field '{field_path}' "
                    f"must be type '{declared_type}', "
                    f"but received '{type(value).__name__}'."
                )
                return 1

            allowed_values_error = validate_allowed_values(
                field_path,
                value,
                field_definition,
            )

            if allowed_values_error:
                print(f"ERROR: {allowed_values_error}")
                return 1

            if declared_type == "list":
                error = validate_list_items(
                    tier_name,
                    field_name,
                    value,
                    field_definition,
                )

                if error:
                    print(f"ERROR: {error}")
                    return 1

            if declared_type == "object":
                error = validate_object_properties(
                    tier_name,
                    field_name,
                    value,
                    field_definition,
                )

                if error:
                    print(f"ERROR: {error}")
                    return 1

    print("OK: All YAML files parsed successfully.")
    print("OK: Expected MetaRCI roots are present.")
    print("OK: Reference, Context, and Interpretive tiers are present.")
    print("OK: Profile document structure is valid.")
    print("OK: Profile extends the loaded base schema.")
    print("OK: Profile implementation metadata is valid.")
    print("OK: Base and profile schema definitions are valid.")
    print("OK: Profile overrides target declared base fields.")
    print("OK: Profile overrides and custom fields were resolved.")
    print("OK: Record profile version matches the profile.")
    print("OK: Required fields are present across all tiers.")
    print("OK: Record fields are declared by the resolved profile.")
    print("OK: Record field values match their declared types.")
    print("OK: Declared allowed values are satisfied.")
    print("OK: List items match their declared item types.")
    print("OK: Nested object properties match their declared schemas.")
    print("OK: Object items in lists match their declared schemas.")

    return 0


if __name__ == "__main__":
    sys.exit(main())