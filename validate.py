from argparse import ArgumentParser, Namespace
from datetime import date, datetime
from pathlib import Path
import sys

import yaml


DEFAULT_FILES = {
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

VALID_OVERRIDE_ATTRIBUTES = {
    "requirement",
    "nullable",
    "description",
    "allowed_values",
}

REQUIREMENT_STRENGTH = {
    "optional": 0,
    "conditional": 1,
    "recommended": 2,
    "required": 3,
}

VALID_BASE_ATTRIBUTES = {
    "name",
    "version",
    "status",
    "description",
    "principles",
    "tiers",
}

REQUIRED_BASE_ATTRIBUTES = {
    "name",
    "version",
    "status",
    "description",
    "tiers",
}

VALID_BASE_STATUSES = {
    "draft",
    "active",
    "deprecated",
    "retired",
}

VALID_TIER_ATTRIBUTES = {
    "name",
    "description",
    "fields",
}

REQUIRED_TIER_ATTRIBUTES = {
    "name",
    "description",
    "fields",
}

VALID_PROFILE_ATTRIBUTES = {
    "name",
    "version",
    "status",
    "extends",
    "base_version",
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
    "base_version",
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

VALID_RECORD_ATTRIBUTES = {
    "profile",
    "profile_version",
    "reference",
    "context",
    "interpretive",
}

REQUIRED_RECORD_ATTRIBUTES = {
    "profile",
    "profile_version",
    "reference",
    "context",
    "interpretive",
}


def parse_arguments() -> Namespace:
    """
    Parse command-line file arguments.

    Each argument has a default, so running `python validate.py`
    continues to validate the repository's example files.
    """
    parser = ArgumentParser(
        description=(
            "Validate a MetaRCI base schema, implementation profile, "
            "and metadata record."
        )
    )

    parser.add_argument(
        "--base",
        type=Path,
        default=DEFAULT_FILES["base"],
        help=(
            "Path to the MetaRCI base-schema YAML file. "
            f"Default: {DEFAULT_FILES['base']}"
        ),
    )

    parser.add_argument(
        "--profile",
        type=Path,
        default=DEFAULT_FILES["profile"],
        help=(
            "Path to the MetaRCI profile YAML file. "
            f"Default: {DEFAULT_FILES['profile']}"
        ),
    )

    parser.add_argument(
        "--record",
        type=Path,
        default=DEFAULT_FILES["record"],
        help=(
            "Path to the MetaRCI record YAML file. "
            f"Default: {DEFAULT_FILES['record']}"
        ),
    )

    return parser.parse_args()


def load_yaml(path: Path) -> dict:
    """Load one YAML file and confirm its root is a mapping."""
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    if not path.is_file():
        raise ValueError(
            f"Expected a file path, but received: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"Expected a YAML mapping in {path}"
        )

    return data


def print_errors(
    stage_name: str,
    errors: list[str],
) -> None:
    """Print all errors collected during one validation stage."""
    print(
        f"VALIDATION FAILED: {stage_name} "
        f"reported {len(errors)} error(s)."
    )

    for index, error in enumerate(errors, start=1):
        print(f"  {index}. {error}")


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
    """Accept a parsed YAML datetime or ISO 8601 datetime string."""
    if isinstance(value, datetime):
        return True

    if isinstance(value, str):
        try:
            datetime.fromisoformat(value)
            return True
        except ValueError:
            return False

    return False


def value_matches_type(
    value: object,
    declared_type: str,
) -> bool:
    """Compare a Python value with a declared MetaRCI type."""
    if declared_type == "string":
        return isinstance(value, str)

    if declared_type == "integer":
        return (
            isinstance(value, int)
            and not isinstance(value, bool)
        )

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
) -> list[str]:
    """Validate a value against allowed_values when declared."""
    errors = []

    allowed_values = definition.get("allowed_values")

    if allowed_values is None:
        return errors

    if not isinstance(allowed_values, list):
        errors.append(
            f"Schema definition for '{path_name}' declares "
            "allowed_values, but allowed_values is not a list."
        )
        return errors

    if value not in allowed_values:
        allowed_display = ", ".join(
            repr(allowed_value)
            for allowed_value in allowed_values
        )

        errors.append(
            f"Value for '{path_name}' must be one of: "
            f"{allowed_display}. Received {value!r}."
        )

    return errors


def validate_base_document(
    base_data: dict,
) -> list[str]:
    """Validate the base schema's top-level document structure."""
    errors = []

    if not isinstance(base_data, dict):
        return ["The metarci value must be a mapping."]

    unknown_attributes = (
        set(base_data)
        - VALID_BASE_ATTRIBUTES
    )

    if unknown_attributes:
        errors.append(
            "Unknown base-schema attributes: "
            + ", ".join(sorted(unknown_attributes))
        )

    missing_attributes = (
        REQUIRED_BASE_ATTRIBUTES
        - set(base_data)
    )

    if missing_attributes:
        errors.append(
            "Base schema is missing required attributes: "
            + ", ".join(sorted(missing_attributes))
        )

    for attribute_name in (
        "name",
        "version",
        "status",
        "description",
    ):
        if attribute_name not in base_data:
            continue

        attribute_value = base_data[attribute_name]

        if not isinstance(attribute_value, str):
            errors.append(
                f"Base-schema attribute '{attribute_name}' "
                "must be a string."
            )
        elif not attribute_value.strip():
            errors.append(
                f"Base-schema attribute '{attribute_name}' "
                "cannot be empty."
            )

    status = base_data.get("status")

    if (
        isinstance(status, str)
        and status not in VALID_BASE_STATUSES
    ):
        allowed_display = ", ".join(
            sorted(VALID_BASE_STATUSES)
        )

        errors.append(
            "Base-schema status must be one of: "
            f"{allowed_display}. Received {status!r}."
        )

    principles = base_data.get("principles", [])

    if not isinstance(principles, list):
        errors.append(
            "Base-schema principles must be a list."
        )
    else:
        for index, principle in enumerate(principles):
            if not isinstance(principle, str):
                errors.append(
                    f"Base-schema principle {index} "
                    "must be a string."
                )
            elif not principle.strip():
                errors.append(
                    f"Base-schema principle {index} "
                    "cannot be empty."
                )

    tiers = base_data.get("tiers")

    if tiers is None:
        return errors

    if not isinstance(tiers, dict):
        errors.append(
            "Base-schema tiers must be a mapping."
        )
        return errors

    tier_names = set(tiers)

    missing_tiers = REQUIRED_TIERS - tier_names
    unknown_tiers = tier_names - REQUIRED_TIERS

    if missing_tiers:
        errors.append(
            "Base schema is missing tiers: "
            + ", ".join(sorted(missing_tiers))
        )

    if unknown_tiers:
        errors.append(
            "Base schema contains unknown tiers: "
            + ", ".join(sorted(unknown_tiers))
        )

    for tier_name in sorted(
        REQUIRED_TIERS & tier_names
    ):
        tier_definition = tiers[tier_name]

        if not isinstance(tier_definition, dict):
            errors.append(
                f"Base tier '{tier_name}' must be a mapping."
            )
            continue

        unknown_tier_attributes = (
            set(tier_definition)
            - VALID_TIER_ATTRIBUTES
        )

        if unknown_tier_attributes:
            errors.append(
                f"Unknown attributes in base tier "
                f"'{tier_name}': "
                + ", ".join(
                    sorted(unknown_tier_attributes)
                )
            )

        missing_tier_attributes = (
            REQUIRED_TIER_ATTRIBUTES
            - set(tier_definition)
        )

        if missing_tier_attributes:
            errors.append(
                f"Base tier '{tier_name}' is missing "
                "attributes: "
                + ", ".join(
                    sorted(missing_tier_attributes)
                )
            )

        for attribute_name in ("name", "description"):
            if attribute_name not in tier_definition:
                continue

            attribute_value = tier_definition[
                attribute_name
            ]

            if not isinstance(attribute_value, str):
                errors.append(
                    f"Base tier '{tier_name}' attribute "
                    f"'{attribute_name}' must be a string."
                )
            elif not attribute_value.strip():
                errors.append(
                    f"Base tier '{tier_name}' attribute "
                    f"'{attribute_name}' cannot be empty."
                )

        fields = tier_definition.get("fields")

        if fields is None:
            continue

        if not isinstance(fields, dict):
            errors.append(
                f"Base tier '{tier_name}' fields "
                "must be a mapping."
            )
        elif not fields:
            errors.append(
                f"Base tier '{tier_name}' must declare "
                "at least one field."
            )

    return errors


def validate_profile_document(
    profile_data: dict,
    profile_path: Path,
    expected_base_path: Path,
) -> list[str]:
    """Validate the profile's top-level document structure."""
    errors = []

    if not isinstance(profile_data, dict):
        return [
            "The metarci_profile value must be a mapping."
        ]

    unknown_attributes = (
        set(profile_data)
        - VALID_PROFILE_ATTRIBUTES
    )

    if unknown_attributes:
        errors.append(
            "Unknown profile attributes: "
            + ", ".join(sorted(unknown_attributes))
        )

    missing_attributes = (
        REQUIRED_PROFILE_ATTRIBUTES
        - set(profile_data)
    )

    if missing_attributes:
        errors.append(
            "Profile is missing required attributes: "
            + ", ".join(sorted(missing_attributes))
        )

    for attribute_name in sorted(
        REQUIRED_PROFILE_ATTRIBUTES
    ):
        if attribute_name not in profile_data:
            continue

        attribute_value = profile_data[attribute_name]

        if not isinstance(attribute_value, str):
            errors.append(
                f"Profile attribute '{attribute_name}' "
                "must be a string."
            )
        elif not attribute_value.strip():
            errors.append(
                f"Profile attribute '{attribute_name}' "
                "cannot be empty."
            )

    status = profile_data.get("status")

    if (
        isinstance(status, str)
        and status not in VALID_PROFILE_STATUSES
    ):
        allowed_display = ", ".join(
            sorted(VALID_PROFILE_STATUSES)
        )

        errors.append(
            "Profile status must be one of: "
            f"{allowed_display}. Received {status!r}."
        )

    description = profile_data.get("description")

    if (
        description is not None
        and not isinstance(description, str)
    ):
        errors.append(
            "Profile description must be a string."
        )

    extends_value = profile_data.get("extends")

    if isinstance(extends_value, str) and extends_value:
        declared_base_path = (
            profile_path.parent / extends_value
        ).resolve()

        loaded_base_path = expected_base_path.resolve()

        if declared_base_path != loaded_base_path:
            errors.append(
                "Profile extends path does not match the "
                "base schema loaded by the validator. "
                f"Profile resolves to '{declared_base_path}', "
                f"but validator loaded '{loaded_base_path}'."
            )

    implementation = profile_data.get(
        "implementation",
        {},
    )

    if not isinstance(implementation, dict):
        errors.append(
            "Profile implementation must be a mapping."
        )
    else:
        unknown_implementation_attributes = (
            set(implementation)
            - VALID_IMPLEMENTATION_ATTRIBUTES
        )

        if unknown_implementation_attributes:
            errors.append(
                "Unknown implementation attributes: "
                + ", ".join(
                    sorted(
                        unknown_implementation_attributes
                    )
                )
            )

        for (
            attribute_name,
            attribute_value,
        ) in implementation.items():
            if (
                attribute_value is not None
                and not isinstance(attribute_value, str)
            ):
                errors.append(
                    f"Profile implementation."
                    f"{attribute_name} must be "
                    "a string or null."
                )

    tier_overrides = profile_data.get(
        "tier_overrides",
        {},
    )

    if not isinstance(tier_overrides, dict):
        errors.append(
            "Profile tier_overrides must be a mapping."
        )

    custom_fields = profile_data.get(
        "custom_fields",
        {},
    )

    if not isinstance(custom_fields, dict):
        errors.append(
            "Profile custom_fields must be a mapping."
        )

    return errors


def validate_record_document(
    record_data: dict,
    record_path: Path,
    expected_profile_path: Path,
) -> list[str]:
    """Validate the record's top-level document structure."""
    errors = []

    if not isinstance(record_data, dict):
        return [
            "The metarci_record value must be a mapping."
        ]

    unknown_attributes = (
        set(record_data)
        - VALID_RECORD_ATTRIBUTES
    )

    if unknown_attributes:
        errors.append(
            "Unknown record attributes: "
            + ", ".join(sorted(unknown_attributes))
        )

    missing_attributes = (
        REQUIRED_RECORD_ATTRIBUTES
        - set(record_data)
    )

    if missing_attributes:
        errors.append(
            "Record is missing required attributes: "
            + ", ".join(sorted(missing_attributes))
        )

    for attribute_name in (
        "profile",
        "profile_version",
    ):
        if attribute_name not in record_data:
            continue

        attribute_value = record_data[attribute_name]

        if not isinstance(attribute_value, str):
            errors.append(
                f"Record attribute '{attribute_name}' "
                "must be a string."
            )
        elif not attribute_value.strip():
            errors.append(
                f"Record attribute '{attribute_name}' "
                "cannot be empty."
            )

    profile_value = record_data.get("profile")

    if isinstance(profile_value, str) and profile_value:
        declared_profile_path = (
            record_path.parent / profile_value
        ).resolve()

        loaded_profile_path = (
            expected_profile_path.resolve()
        )

        if declared_profile_path != loaded_profile_path:
            errors.append(
                "Record profile path does not match the "
                "profile loaded by the validator. "
                f"Record resolves to "
                f"'{declared_profile_path}', but validator "
                f"loaded '{loaded_profile_path}'."
            )

    for tier_name in sorted(REQUIRED_TIERS):
        if tier_name not in record_data:
            continue

        tier_value = record_data[tier_name]

        if not isinstance(tier_value, dict):
            errors.append(
                f"Record tier '{tier_name}' "
                "must be a mapping."
            )

    return errors


def validate_field_definition(
    path_name: str,
    field_definition: object,
) -> list[str]:
    """Recursively validate one schema field definition."""
    errors = []

    if not isinstance(field_definition, dict):
        return [
            f"Schema definition for '{path_name}' "
            "must be a mapping."
        ]

    unknown_attributes = (
        set(field_definition)
        - VALID_FIELD_ATTRIBUTES
    )

    if unknown_attributes:
        errors.append(
            f"Unknown schema attributes for "
            f"'{path_name}': "
            + ", ".join(sorted(unknown_attributes))
        )

    declared_type = field_definition.get("type")

    if declared_type not in VALID_TYPES:
        errors.append(
            f"Schema field '{path_name}' must declare "
            f"one of {sorted(VALID_TYPES)} as its type. "
            f"Received {declared_type!r}."
        )

    requirement = field_definition.get("requirement")

    if requirement not in VALID_REQUIREMENTS:
        errors.append(
            f"Schema field '{path_name}' must declare "
            f"one of {sorted(VALID_REQUIREMENTS)} "
            f"as its requirement. "
            f"Received {requirement!r}."
        )

    nullable = field_definition.get("nullable")

    if not isinstance(nullable, bool):
        errors.append(
            f"Schema field '{path_name}' must declare "
            "nullable as true or false."
        )

    description = field_definition.get("description")

    if (
        description is not None
        and not isinstance(description, str)
    ):
        errors.append(
            f"Schema field '{path_name}' has a "
            "description that is not a string."
        )

    allowed_values = field_definition.get(
        "allowed_values"
    )

    if (
        allowed_values is not None
        and not isinstance(allowed_values, list)
    ):
        errors.append(
            f"Schema field '{path_name}' declares "
            "allowed_values, but allowed_values "
            "is not a list."
        )

    if declared_type == "list":
        item_type = field_definition.get("item_type")

        if item_type not in VALID_TYPES:
            errors.append(
                f"List field '{path_name}' must declare "
                f"a valid item_type. "
                f"Received {item_type!r}."
            )

        item_properties = field_definition.get(
            "item_properties"
        )

        if item_type == "object":
            if not isinstance(item_properties, dict):
                errors.append(
                    f"Object-list field '{path_name}' "
                    "must declare item_properties "
                    "as a mapping."
                )
            else:
                for (
                    property_name,
                    property_definition,
                ) in item_properties.items():
                    errors.extend(
                        validate_field_definition(
                            (
                                f"{path_name}[]"
                                f".{property_name}"
                            ),
                            property_definition,
                        )
                    )

        elif item_properties is not None:
            errors.append(
                f"List field '{path_name}' declares "
                "item_properties, but its item_type "
                "is not 'object'."
            )

    else:
        if "item_type" in field_definition:
            errors.append(
                f"Non-list field '{path_name}' "
                "cannot declare item_type."
            )

        if "item_properties" in field_definition:
            errors.append(
                f"Non-list field '{path_name}' "
                "cannot declare item_properties."
            )

    if declared_type == "object":
        properties = field_definition.get("properties")

        if properties is not None:
            if not isinstance(properties, dict):
                errors.append(
                    f"Object field '{path_name}' must "
                    "declare properties as a mapping."
                )
            else:
                for (
                    property_name,
                    property_definition,
                ) in properties.items():
                    errors.extend(
                        validate_field_definition(
                            (
                                f"{path_name}."
                                f"{property_name}"
                            ),
                            property_definition,
                        )
                    )

    elif "properties" in field_definition:
        errors.append(
            f"Non-object field '{path_name}' "
            "cannot declare properties."
        )

    return errors


def validate_override_definition(
    path_name: str,
    base_definition: dict,
    override_definition: object,
) -> list[str]:
    """
    Validate one profile override against its base field.

    MetaRCI 0.1 permits only shallow, non-structural overrides.
    Profiles may strengthen constraints but may not weaken or
    structurally redefine fields declared by the base schema.
    """
    errors = []

    if not isinstance(override_definition, dict):
        return [
            f"Override for '{path_name}' must be a mapping."
        ]

    unsupported_attributes = (
        set(override_definition)
        - VALID_OVERRIDE_ATTRIBUTES
    )

    if unsupported_attributes:
        errors.append(
            f"Unsupported override attributes for "
            f"'{path_name}': "
            + ", ".join(sorted(unsupported_attributes))
            + ". MetaRCI 0.1 permits overrides only for: "
            + ", ".join(sorted(VALID_OVERRIDE_ATTRIBUTES))
            + "."
        )

    if "requirement" in override_definition:
        override_requirement = override_definition[
            "requirement"
        ]

        if override_requirement not in VALID_REQUIREMENTS:
            errors.append(
                f"Override for '{path_name}' declares "
                f"invalid requirement "
                f"{override_requirement!r}."
            )
        else:
            base_requirement = base_definition.get(
                "requirement"
            )

            if base_requirement in REQUIREMENT_STRENGTH:
                base_strength = REQUIREMENT_STRENGTH[
                    base_requirement
                ]

                override_strength = REQUIREMENT_STRENGTH[
                    override_requirement
                ]

                if override_strength < base_strength:
                    errors.append(
                        f"Override for '{path_name}' weakens "
                        f"requirement from "
                        f"'{base_requirement}' to "
                        f"'{override_requirement}'. "
                        "Profiles may strengthen requirements "
                        "but may not weaken them."
                    )

    if "nullable" in override_definition:
        override_nullable = override_definition["nullable"]

        if not isinstance(override_nullable, bool):
            errors.append(
                f"Override for '{path_name}' must declare "
                "nullable as true or false."
            )
        else:
            base_nullable = base_definition.get("nullable")

            if (
                base_nullable is False
                and override_nullable is True
            ):
                errors.append(
                    f"Override for '{path_name}' changes a "
                    "non-nullable base field to nullable. "
                    "Profiles may make nullable fields "
                    "non-nullable but may not weaken "
                    "base nullability."
                )

    if "description" in override_definition:
        override_description = override_definition[
            "description"
        ]

        if not isinstance(override_description, str):
            errors.append(
                f"Override for '{path_name}' has a "
                "description that is not a string."
            )
        elif not override_description.strip():
            errors.append(
                f"Override for '{path_name}' has an "
                "empty description."
            )

    if "allowed_values" in override_definition:
        override_allowed_values = override_definition[
            "allowed_values"
        ]

        if not isinstance(override_allowed_values, list):
            errors.append(
                f"Override for '{path_name}' declares "
                "allowed_values that is not a list."
            )
        else:
            base_allowed_values = base_definition.get(
                "allowed_values"
            )

            if base_allowed_values is None:
                errors.append(
                    f"Override for '{path_name}' declares "
                    "allowed_values, but the base field does "
                    "not define an allowed-values set. "
                    "MetaRCI 0.1 permits profiles to narrow "
                    "existing allowed values, not introduce "
                    "a new controlled vocabulary through "
                    "an override."
                )

            elif not isinstance(base_allowed_values, list):
                errors.append(
                    f"Base field '{path_name}' has invalid "
                    "allowed_values and cannot be safely "
                    "overridden."
                )

            else:
                unsupported_values = [
                    value
                    for value in override_allowed_values
                    if value not in base_allowed_values
                ]

                if unsupported_values:
                    unsupported_display = ", ".join(
                        repr(value)
                        for value in unsupported_values
                    )

                    errors.append(
                        f"Override for '{path_name}' expands "
                        "the base allowed-values set with: "
                        f"{unsupported_display}. Profiles "
                        "may only narrow allowed_values."
                    )

    return errors


def validate_schema_definitions(
    base_data: dict,
    profile_data: dict,
) -> list[str]:
    """
    Validate base fields, profile custom fields, and overrides.

    Profile overrides are intentionally restricted in MetaRCI 0.1.
    They may strengthen non-structural field constraints but may
    not redefine the base schema's field shapes.
    """
    errors = []

    for tier_name in sorted(REQUIRED_TIERS):
        fields = (
            base_data["tiers"][tier_name]["fields"]
        )

        for (
            field_name,
            field_definition,
        ) in fields.items():
            errors.extend(
                validate_field_definition(
                    f"{tier_name}.{field_name}",
                    field_definition,
                )
            )

    custom_fields = profile_data.get(
        "custom_fields",
        {},
    )

    if isinstance(custom_fields, dict):
        unknown_custom_tiers = (
            set(custom_fields)
            - REQUIRED_TIERS
        )

        if unknown_custom_tiers:
            errors.append(
                "Unknown custom-field tiers: "
                + ", ".join(
                    sorted(unknown_custom_tiers)
                )
            )

        for tier_name in sorted(REQUIRED_TIERS):
            tier_custom_fields = custom_fields.get(
                tier_name,
                {},
            )

            if not isinstance(tier_custom_fields, dict):
                errors.append(
                    f"Profile custom_fields.{tier_name} "
                    "must be a mapping."
                )
                continue

            base_fields = (
                base_data["tiers"][tier_name]["fields"]
            )

            duplicate_field_names = (
                set(tier_custom_fields)
                & set(base_fields)
            )

            if duplicate_field_names:
                errors.append(
                    f"Custom fields in the {tier_name} tier "
                    "duplicate fields declared by the base "
                    "schema: "
                    + ", ".join(
                        sorted(duplicate_field_names)
                    )
                    + ". Use tier_overrides to specialize "
                    "an existing base field."
                )

            for (
                field_name,
                field_definition,
            ) in tier_custom_fields.items():
                if field_name in base_fields:
                    continue

                errors.extend(
                    validate_field_definition(
                        f"{tier_name}.{field_name}",
                        field_definition,
                    )
                )

    tier_overrides = profile_data.get(
        "tier_overrides",
        {},
    )

    if isinstance(tier_overrides, dict):
        unknown_override_tiers = (
            set(tier_overrides)
            - REQUIRED_TIERS
        )

        if unknown_override_tiers:
            errors.append(
                "Unknown override tiers: "
                + ", ".join(
                    sorted(unknown_override_tiers)
                )
            )

        for tier_name, overrides in (
            tier_overrides.items()
        ):
            if tier_name not in REQUIRED_TIERS:
                continue

            if not isinstance(overrides, dict):
                errors.append(
                    f"Profile tier_overrides."
                    f"{tier_name} must be a mapping."
                )
                continue

            base_fields = (
                base_data["tiers"][tier_name]["fields"]
            )

            unknown_override_fields = (
                set(overrides)
                - set(base_fields)
            )

            if unknown_override_fields:
                errors.append(
                    f"Unknown field overrides in "
                    f"{tier_name} tier: "
                    + ", ".join(
                        sorted(unknown_override_fields)
                    )
                )

            for (
                field_name,
                override_definition,
            ) in overrides.items():
                if field_name not in base_fields:
                    continue

                errors.extend(
                    validate_override_definition(
                        f"{tier_name}.{field_name}",
                        base_fields[field_name],
                        override_definition,
                    )
                )

    return errors


def resolve_field_definitions(
    base_data: dict,
    profile_data: dict,
    tier_name: str,
) -> dict:
    """Resolve base fields, profile overrides, and custom fields."""
    base_fields = (
        base_data["tiers"][tier_name]["fields"]
    )

    tier_overrides = (
        profile_data
        .get("tier_overrides", {})
        .get(tier_name, {})
    )

    custom_fields = (
        profile_data
        .get("custom_fields", {})
        .get(tier_name, {})
    )

    resolved_fields = {}

    for (
        field_name,
        field_definition,
    ) in base_fields.items():
        resolved_definition = dict(
            field_definition
        )

        if field_name in tier_overrides:
            resolved_definition.update(
                tier_overrides[field_name]
            )

        resolved_fields[field_name] = (
            resolved_definition
        )

    resolved_fields.update(custom_fields)

    return resolved_fields


def validate_value(
    path_name: str,
    value: object,
    definition: dict,
) -> list[str]:
    """Recursively validate one record value."""
    errors = []

    nullable = definition["nullable"]

    if value is None:
        if not nullable:
            errors.append(
                f"Value '{path_name}' is null but "
                "is not nullable."
            )

        return errors

    declared_type = definition["type"]

    if not value_matches_type(
        value,
        declared_type,
    ):
        errors.append(
            f"Value '{path_name}' must be type "
            f"'{declared_type}', but received "
            f"'{type(value).__name__}'."
        )

        return errors

    errors.extend(
        validate_allowed_values(
            path_name,
            value,
            definition,
        )
    )

    if declared_type == "list":
        item_type = definition["item_type"]
        item_properties = definition.get(
            "item_properties",
            {},
        )

        for index, item in enumerate(value):
            item_path = f"{path_name}[{index}]"

            item_definition = {
                "type": item_type,
                "requirement": "required",
                "nullable": False,
            }

            if item_type == "object":
                item_definition["properties"] = (
                    item_properties
                )

            errors.extend(
                validate_value(
                    item_path,
                    item,
                    item_definition,
                )
            )

    if declared_type == "object":
        property_definitions = definition.get(
            "properties",
            {},
        )

        if not property_definitions:
            return errors

        unknown_properties = (
            set(value)
            - set(property_definitions)
        )

        if unknown_properties:
            errors.append(
                f"Unknown properties in '{path_name}': "
                + ", ".join(
                    sorted(unknown_properties)
                )
            )

        required_properties = {
            property_name
            for (
                property_name,
                property_definition,
            ) in property_definitions.items()
            if (
                property_definition.get("requirement")
                == "required"
            )
        }

        missing_required_properties = {
            property_name
            for property_name in required_properties
            if (
                property_name not in value
                or value[property_name] is None
            )
        }

        if missing_required_properties:
            errors.append(
                f"Missing required properties in "
                f"'{path_name}': "
                + ", ".join(
                    sorted(
                        missing_required_properties
                    )
                )
            )

        for (
            property_name,
            property_value,
        ) in value.items():
            if property_name not in property_definitions:
                continue

            property_definition = (
                property_definitions[property_name]
            )

            errors.extend(
                validate_value(
                    (
                        f"{path_name}."
                        f"{property_name}"
                    ),
                    property_value,
                    property_definition,
                )
            )

    return errors


def main() -> int:
    args = parse_arguments()

    files = {
        "base": args.base,
        "profile": args.profile,
        "record": args.record,
    }

    try:
        documents = {
            name: load_yaml(path)
            for name, path in files.items()
        }
    except (
        FileNotFoundError,
        ValueError,
        yaml.YAMLError,
        OSError,
    ) as error:
        print(f"ERROR: {error}")
        return 1

    base = documents["base"]
    profile = documents["profile"]
    record = documents["record"]

    root_errors = []

    if "metarci" not in base:
        root_errors.append(
            "Base schema is missing the 'metarci' root."
        )

    if "metarci_profile" not in profile:
        root_errors.append(
            "Profile is missing the "
            "'metarci_profile' root."
        )

    if "metarci_record" not in record:
        root_errors.append(
            "Record is missing the "
            "'metarci_record' root."
        )

    if root_errors:
        print_errors(
            "Root validation",
            root_errors,
        )
        return 1

    base_data = base["metarci"]
    profile_data = profile["metarci_profile"]
    record_data = record["metarci_record"]

    document_errors = []

    document_errors.extend(
        validate_base_document(base_data)
    )

    document_errors.extend(
        validate_profile_document(
            profile_data,
            files["profile"],
            files["base"],
        )
    )

    document_errors.extend(
        validate_record_document(
            record_data,
            files["record"],
            files["profile"],
        )
    )

    if document_errors:
        print_errors(
            "Document validation",
            document_errors,
        )
        return 1

    schema_errors = validate_schema_definitions(
        base_data,
        profile_data,
    )

    if schema_errors:
        print_errors(
            "Schema-definition validation",
            schema_errors,
        )
        return 1

    compatibility_errors = []

    declared_base_version = (
        profile_data["base_version"]
    )

    loaded_base_version = base_data["version"]

    if declared_base_version != loaded_base_version:
        compatibility_errors.append(
            "Profile base_version does not match "
            "the loaded base-schema version. "
            f"Expected '{loaded_base_version}', got "
            f"'{declared_base_version}'."
        )

    declared_profile_version = (
        profile_data["version"]
    )

    record_profile_version = (
        record_data["profile_version"]
    )

    if (
        declared_profile_version
        != record_profile_version
    ):
        compatibility_errors.append(
            "Record profile_version does not match "
            "the profile version. "
            f"Expected '{declared_profile_version}', "
            f"got '{record_profile_version}'."
        )

    if compatibility_errors:
        print_errors(
            "Version compatibility",
            compatibility_errors,
        )
        return 1

    resolved_schemas = {
        tier_name: resolve_field_definitions(
            base_data,
            profile_data,
            tier_name,
        )
        for tier_name in REQUIRED_TIERS
    }

    record_structure_errors = []

    for tier_name in sorted(REQUIRED_TIERS):
        tier_schema = resolved_schemas[tier_name]
        tier_record = record_data[tier_name]

        required_fields = {
            field_name
            for (
                field_name,
                field_definition,
            ) in tier_schema.items()
            if (
                field_definition.get("requirement")
                == "required"
            )
        }

        missing_required_fields = {
            field_name
            for field_name in required_fields
            if (
                field_name not in tier_record
                or tier_record[field_name] is None
            )
        }

        if missing_required_fields:
            record_structure_errors.append(
                f"Missing required fields in "
                f"{tier_name} tier: "
                + ", ".join(
                    sorted(missing_required_fields)
                )
            )

        allowed_fields = set(tier_schema)
        record_fields = set(tier_record)

        unknown_fields = (
            record_fields
            - allowed_fields
        )

        if unknown_fields:
            record_structure_errors.append(
                f"Unknown fields in "
                f"{tier_name} tier: "
                + ", ".join(sorted(unknown_fields))
            )

    if record_structure_errors:
        print_errors(
            "Record structure",
            record_structure_errors,
        )
        return 1

    value_errors = []

    for tier_name in sorted(REQUIRED_TIERS):
        field_definitions = (
            resolved_schemas[tier_name]
        )

        tier_record = record_data[tier_name]

        for (
            field_name,
            value,
        ) in tier_record.items():
            value_errors.extend(
                validate_value(
                    f"{tier_name}.{field_name}",
                    value,
                    field_definitions[field_name],
                )
            )

    if value_errors:
        print_errors(
            "Record-value validation",
            value_errors,
        )
        return 1

    print("OK: All YAML files parsed successfully.")
    print("OK: Expected MetaRCI roots are present.")
    print("OK: Base-schema document structure is valid.")
    print("OK: Base-schema metadata and lifecycle status are valid.")
    print("OK: Base-schema principles are valid.")
    print("OK: Reference, Context, and Interpretive tiers are present.")
    print("OK: Base-tier document structures are valid.")
    print("OK: Profile document structure is valid.")
    print("OK: Profile extends the loaded base schema.")
    print("OK: Profile implementation metadata is valid.")
    print("OK: Record document structure is valid.")
    print("OK: Record references the loaded profile.")
    print("OK: Record tiers are valid mappings.")
    print("OK: Base and profile schema definitions are valid.")
    print("OK: Profile overrides target declared base fields.")
    print("OK: Profile override constraints are satisfied.")
    print("OK: Profile overrides and custom fields were resolved.")
    print("OK: Profile base_version matches the base schema.")
    print("OK: Record profile_version matches the profile.")
    print("OK: Required fields are present across all tiers.")
    print("OK: Record fields are declared by the resolved profile.")
    print("OK: Record values passed recursive type validation.")
    print("OK: Declared allowed values are satisfied.")
    print("OK: Nested lists and objects match their schemas.")
    print("OK: Recursive record validation completed successfully.")
    print("OK: Validation completed with no errors.")
    print()
    print("Validated files:")
    print(f"  Base:    {files['base'].resolve()}")
    print(f"  Profile: {files['profile'].resolve()}")
    print(f"  Record:  {files['record'].resolve()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())