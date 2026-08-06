from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = PROJECT_ROOT / "validate.py"

SOURCE_FILES = {
    "base": PROJECT_ROOT / "schemas" / "metarci-base.yaml",
    "profile": PROJECT_ROOT / "profiles" / "example-profile.yaml",
    "record": PROJECT_ROOT / "examples" / "example-record.yaml",
    "document_profile": PROJECT_ROOT / "profiles" / "document.yaml",
    "document_record": PROJECT_ROOT / "examples" / "document-record.yaml",
    "structured_data_profile": PROJECT_ROOT / "profiles" / "structured-data.yaml",
    "structured_data_record": PROJECT_ROOT / "examples" / "structured-data-record.yaml",
    "media_profile": PROJECT_ROOT / "profiles" / "media.yaml",
    "media_record": PROJECT_ROOT / "examples" / "media-record.yaml",
    "composite_profile": PROJECT_ROOT / "profiles" / "composite.yaml",
    "composite_record": PROJECT_ROOT / "examples" / "composite-record.yaml",
}


class MetaRCIValidatorTests(unittest.TestCase):
    """
    Test the MetaRCI validator through its command-line interface.

    Each test receives temporary copies of the repository's valid
    schema, profile, and record files. Individual tests may modify
    those copies without changing the repository examples.
    """

    def setUp(self) -> None:
        """Create an isolated temporary MetaRCI file structure."""
        self.temp_directory = tempfile.TemporaryDirectory()
        self.temp_root = Path(self.temp_directory.name)

        self.schema_directory = self.temp_root / "schemas"
        self.profile_directory = self.temp_root / "profiles"
        self.example_directory = self.temp_root / "examples"

        self.schema_directory.mkdir()
        self.profile_directory.mkdir()
        self.example_directory.mkdir()

        self.base_path = (
            self.schema_directory / "metarci-base.yaml"
        )

        self.profile_path = (
            self.profile_directory / "example-profile.yaml"
        )

        self.record_path = (
            self.example_directory / "example-record.yaml"
        )

        shutil.copy(
            SOURCE_FILES["base"],
            self.base_path,
        )

        shutil.copy(
            SOURCE_FILES["profile"],
            self.profile_path,
        )

        shutil.copy(
            SOURCE_FILES["record"],
            self.record_path,
        )

    def tearDown(self) -> None:
        """Remove all temporary files created for the test."""
        self.temp_directory.cleanup()

    def load_yaml(self, path: Path) -> dict:
        """Load a temporary YAML document."""
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def save_yaml(
        self,
        path: Path,
        data: dict,
    ) -> None:
        """
        Save modified YAML data.

        Disabling key sorting preserves the original logical order,
        which makes temporary fixtures easier to inspect.
        """
        with path.open("w", encoding="utf-8") as file:
            yaml.safe_dump(
                data,
                file,
                sort_keys=False,
                allow_unicode=True,
            )

    def run_validator(
        self,
    ) -> subprocess.CompletedProcess[str]:
        """
        Run validate.py against the temporary files.

        Calling the public command-line interface verifies argument
        handling as well as the validator itself.
        """
        command = [
            sys.executable,
            str(VALIDATOR_PATH),
            "--base",
            str(self.base_path),
            "--profile",
            str(self.profile_path),
            "--record",
            str(self.record_path),
        ]

        return subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def stage_profile_and_record(
        self,
        profile_source: Path,
        record_source: Path,
    ) -> None:
        """Replace the temporary profile and record with new fixtures."""
        self.profile_path = self.profile_directory / profile_source.name
        self.record_path = self.example_directory / record_source.name

        shutil.copy(profile_source, self.profile_path)
        shutil.copy(record_source, self.record_path)

    def combined_output(
        self,
        result: subprocess.CompletedProcess[str],
    ) -> str:
        """Combine standard output and standard error for assertions."""
        return result.stdout + result.stderr

    # ---------------------------------------------------------
    # Valid baseline
    # ---------------------------------------------------------

    def test_valid_files_pass(self) -> None:
        """The repository's valid example files should pass."""
        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

        self.assertIn(
            "OK: Validation completed with no errors.",
            result.stdout,
        )

    def test_document_profile_and_record_pass(self) -> None:
        """The document profile and record should validate."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_structured_data_profile_and_record_pass(self) -> None:
        """The structured-data profile and record should validate."""
        self.stage_profile_and_record(
            SOURCE_FILES["structured_data_profile"],
            SOURCE_FILES["structured_data_record"],
        )

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_media_profile_and_record_pass(self) -> None:
        """The media profile and record should validate."""
        self.stage_profile_and_record(
            SOURCE_FILES["media_profile"],
            SOURCE_FILES["media_record"],
        )

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_composite_profile_and_record_pass(self) -> None:
        """The composite profile and record should validate."""
        self.stage_profile_and_record(
            SOURCE_FILES["composite_profile"],
            SOURCE_FILES["composite_record"],
        )

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_valid_strengthened_requirement_passes(self) -> None:
        """A profile may strengthen a field requirement."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)
        record = self.load_yaml(self.record_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ]["page_count"]["requirement"] = "required"

        self.save_yaml(self.profile_path, profile)
        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_valid_strengthened_nullability_passes(self) -> None:
        """A profile may make a nullable field non-nullable."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)
        record = self.load_yaml(self.record_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ].setdefault("review_date", {})["nullable"] = False

        self.save_yaml(self.profile_path, profile)
        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_valid_narrowed_allowed_values_passes(self) -> None:
        """A profile may narrow an existing allowed-values set."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)
        record = self.load_yaml(self.record_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ].setdefault("extraction_status", {})[
            "allowed_values"
        ] = [
            "success",
            "partial",
        ]

        self.save_yaml(self.profile_path, profile)
        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_genuinely_new_profile_custom_fields_pass(self) -> None:
        """A new profile custom field should validate when used."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)
        record = self.load_yaml(self.record_path)

        profile["metarci_profile"]["custom_fields"][
            "context"
        ]["local_reference_code"] = {
            "type": "string",
            "requirement": "conditional",
            "nullable": True,
            "description": "Local reference code for the source.",
        }

        record["metarci_record"]["context"][
            "local_reference_code"
        ] = "LOC-001"

        self.save_yaml(self.profile_path, profile)
        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(
            result.returncode,
            0,
            msg=self.combined_output(result),
        )

    def test_invalid_override_type_fails(self) -> None:
        """A structural type override should be rejected."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ]["page_count"]["type"] = "number"

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("Unsupported override attributes", result.stdout)
        self.assertIn("type", result.stdout)

    def test_invalid_override_item_type_fails(self) -> None:
        """A structural item_type override should be rejected."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"]["context"][
            "alternate_titles"
        ] = {
            "item_type": "integer",
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("Unsupported override attributes", result.stdout)
        self.assertIn("item_type", result.stdout)

    def test_invalid_override_properties_fails(self) -> None:
        """A structural properties override should be rejected."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "context"
        ]["sensitivity"] = {
            "properties": {
                "level": {
                    "type": "string",
                }
            }
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("Unsupported override attributes", result.stdout)
        self.assertIn("properties", result.stdout)

    def test_invalid_override_item_properties_fails(self) -> None:
        """A structural item_properties override should be rejected."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "interpretive"
        ]["relationships"] = {
            "item_properties": {
                "target_id": {
                    "type": "string",
                }
            }
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("Unsupported override attributes", result.stdout)
        self.assertIn("item_properties", result.stdout)

    def test_invalid_weakened_requirement_fails(self) -> None:
        """A profile may not weaken a base requirement."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ]["source_id"] = {
            "requirement": "recommended",
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("weakens requirement", result.stdout)
        self.assertIn("source_id", result.stdout)

    def test_invalid_weakened_nullability_fails(self) -> None:
        """A profile may not make a non-nullable base field nullable."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ]["ingestion_timestamp"] = {
            "nullable": True,
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("non-nullable base field to nullable", result.stdout)
        self.assertIn("ingestion_timestamp", result.stdout)

    def test_invalid_allowed_values_expansion_fails(self) -> None:
        """A profile may not expand a base allowed-values set."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ]["extraction_status"] = {
            "allowed_values": [
                "success",
                "partial",
                "queued",
            ]
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("expands the base allowed-values set", result.stdout)
        self.assertIn("queued", result.stdout)

    def test_invalid_allowed_values_introduction_fails(self) -> None:
        """A profile may not invent allowed_values for a base field."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ]["stated_title"] = {
            "allowed_values": [
                "Example Policy Manual",
            ]
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("does not define an allowed-values set", result.stdout)
        self.assertIn("stated_title", result.stdout)

    def test_invalid_custom_field_shadowing_base_fails(self) -> None:
        """A custom field may not duplicate a base field name."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["custom_fields"][
            "reference"
        ]["source_id"] = {
            "type": "string",
            "requirement": "conditional",
            "nullable": True,
            "description": "Shadowed source identifier.",
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate fields declared by the base schema", result.stdout)
        self.assertIn("source_id", result.stdout)

    def test_invalid_override_targeting_undeclared_field_fails(self) -> None:
        """An override cannot target an undeclared base field."""
        self.stage_profile_and_record(
            SOURCE_FILES["document_profile"],
            SOURCE_FILES["document_record"],
        )

        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "context"
        ]["imaginary_field"] = {
            "requirement": "required",
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)
        self.assertIn("Unknown field overrides in context tier", result.stdout)
        self.assertIn("imaginary_field", result.stdout)

    # ---------------------------------------------------------
    # Record value validation
    # ---------------------------------------------------------

    def test_invalid_allowed_value_fails(self) -> None:
        """An invalid controlled value should be rejected."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["reference"][
            "extraction_status"
        ] = "complete"

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Record-value validation",
            result.stdout,
        )

        self.assertIn(
            "reference.extraction_status",
            result.stdout,
        )

        self.assertIn(
            "Received 'complete'",
            result.stdout,
        )

    def test_wrong_field_type_fails(self) -> None:
        """A string supplied for an integer field should fail."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["reference"][
            "page_count"
        ] = "twelve"

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "reference.page_count",
            result.stdout,
        )

        self.assertIn(
            "must be type 'integer'",
            result.stdout,
        )

    def test_nested_sensitivity_item_type_fails(self) -> None:
        """A malformed nested sensitivity list item should fail."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["context"][
            "sensitivity"
        ]["categories"] = [
            "business-sensitive",
            42,
        ]

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Record-value validation",
            result.stdout,
        )

        self.assertIn(
            "context.sensitivity.categories[1]",
            result.stdout,
        )

        self.assertIn(
            "must be type 'string'",
            result.stdout,
        )

    def test_relationship_missing_required_property_fails(
        self,
    ) -> None:
        """A relationship without target_id should fail."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["interpretive"][
            "relationships"
        ] = [
            {
                "relationship_type": "supports",
                "notes": "Example relationship.",
            }
        ]

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Record-value validation",
            result.stdout,
        )

        self.assertIn(
            "interpretive.relationships[0]",
            result.stdout,
        )

        self.assertIn(
            "target_id",
            result.stdout,
        )

    def test_relationship_property_type_fails(self) -> None:
        """A relationship property with the wrong type should fail."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["interpretive"][
            "relationships"
        ] = [
            {
                "target_id": "example-002",
                "relationship_type": 42,
                "notes": None,
            }
        ]

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "interpretive.relationships[0].relationship_type",
            result.stdout,
        )

        self.assertIn(
            "must be type 'string'",
            result.stdout,
        )

    def test_multiple_value_errors_are_aggregated(
        self,
    ) -> None:
        """Independent value errors should appear in one report."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["reference"][
            "page_count"
        ] = "twelve"

        record["metarci_record"]["reference"][
            "extraction_status"
        ] = "complete"

        record["metarci_record"]["context"][
            "alternate_titles"
        ] = [
            "Valid alternate title",
            42,
        ]

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "reported 3 error(s)",
            result.stdout,
        )

        self.assertIn(
            "reference.page_count",
            result.stdout,
        )

        self.assertIn(
            "reference.extraction_status",
            result.stdout,
        )

        self.assertIn(
            "context.alternate_titles[1]",
            result.stdout,
        )

    # ---------------------------------------------------------
    # Record structure validation
    # ---------------------------------------------------------

    def test_missing_required_field_fails(self) -> None:
        """A required record field should not be removable."""
        record = self.load_yaml(self.record_path)

        del record["metarci_record"]["reference"][
            "source_id"
        ]

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Record structure",
            result.stdout,
        )

        self.assertIn(
            "source_id",
            result.stdout,
        )

    def test_unknown_record_field_fails(self) -> None:
        """An undeclared record field should be rejected."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["context"][
            "mystery_field"
        ] = "unexpected"

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Record structure",
            result.stdout,
        )

        self.assertIn(
            "mystery_field",
            result.stdout,
        )

    def test_record_tier_must_be_mapping(self) -> None:
        """A record tier cannot be replaced with a list."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"]["context"] = [
            "not",
            "a",
            "mapping",
        ]

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Document validation",
            result.stdout,
        )

        self.assertIn(
            "Record tier 'context' must be a mapping",
            result.stdout,
        )

    # ---------------------------------------------------------
    # Version compatibility
    # ---------------------------------------------------------

    def test_profile_base_version_mismatch_fails(
        self,
    ) -> None:
        """A profile written for another base version should fail."""
        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"][
            "base_version"
        ] = "9.9.9"

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Version compatibility",
            result.stdout,
        )

        self.assertIn(
            "Profile base_version does not match",
            result.stdout,
        )

    def test_record_profile_version_mismatch_fails(
        self,
    ) -> None:
        """A record using another profile version should fail."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"][
            "profile_version"
        ] = "9.9.9"

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Version compatibility",
            result.stdout,
        )

        self.assertIn(
            "Record profile_version does not match",
            result.stdout,
        )

    # ---------------------------------------------------------
    # Schema-definition validation
    # ---------------------------------------------------------

    def test_invalid_base_field_type_fails(self) -> None:
        """An unsupported schema type should be rejected."""
        base = self.load_yaml(self.base_path)

        base["metarci"]["tiers"]["reference"]["fields"][
            "page_count"
        ]["type"] = "number"

        self.save_yaml(self.base_path, base)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Schema-definition validation",
            result.stdout,
        )

        self.assertIn(
            "reference.page_count",
            result.stdout,
        )

        self.assertIn(
            "Received 'number'",
            result.stdout,
        )

    def test_missing_nested_requirement_fails(self) -> None:
        """Nested properties must declare requirement behavior."""
        base = self.load_yaml(self.base_path)

        del base["metarci"]["tiers"]["context"]["fields"][
            "sensitivity"
        ]["properties"]["level"]["requirement"]

        self.save_yaml(self.base_path, base)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Schema-definition validation",
            result.stdout,
        )

        self.assertIn(
            "context.sensitivity.level",
            result.stdout,
        )

        self.assertIn(
            "Received None",
            result.stdout,
        )

    def test_invalid_profile_override_fails(self) -> None:
        """An invalid requirement override should be rejected."""
        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "reference"
        ]["review_date"]["requirement"] = "mandatory"

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Schema-definition validation",
            result.stdout,
        )

        self.assertIn(
            "reference.review_date",
            result.stdout,
        )

        self.assertIn(
            "mandatory",
            result.stdout,
        )

    def test_unknown_override_field_fails(self) -> None:
        """An override cannot target an undeclared base field."""
        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"]["tier_overrides"][
            "context"
        ]["imaginary_field"] = {
            "requirement": "required",
        }

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Schema-definition validation",
            result.stdout,
        )

        self.assertIn(
            "imaginary_field",
            result.stdout,
        )

    # ---------------------------------------------------------
    # Path validation
    # ---------------------------------------------------------

    def test_profile_extends_wrong_base_path_fails(
        self,
    ) -> None:
        """The profile must extend the loaded base file."""
        profile = self.load_yaml(self.profile_path)

        profile["metarci_profile"][
            "extends"
        ] = "../schemas/another-schema.yaml"

        self.save_yaml(self.profile_path, profile)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Document validation",
            result.stdout,
        )

        self.assertIn(
            "Profile extends path does not match",
            result.stdout,
        )

    def test_record_references_wrong_profile_path_fails(
        self,
    ) -> None:
        """The record must reference the loaded profile file."""
        record = self.load_yaml(self.record_path)

        record["metarci_record"][
            "profile"
        ] = "../profiles/another-profile.yaml"

        self.save_yaml(self.record_path, record)

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Document validation",
            result.stdout,
        )

        self.assertIn(
            "Record profile path does not match",
            result.stdout,
        )

    # ---------------------------------------------------------
    # Root and YAML parsing validation
    # ---------------------------------------------------------

    def test_missing_base_root_fails(self) -> None:
        """The base document must use the metarci root."""
        base = self.load_yaml(self.base_path)

        malformed_base = {
            "wrong_root": base["metarci"],
        }

        self.save_yaml(
            self.base_path,
            malformed_base,
        )

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Root validation",
            result.stdout,
        )

        self.assertIn(
            "missing the 'metarci' root",
            result.stdout,
        )

    def test_missing_profile_root_fails(self) -> None:
        """The profile document must use metarci_profile."""
        profile = self.load_yaml(self.profile_path)

        malformed_profile = {
            "wrong_root": profile["metarci_profile"],
        }

        self.save_yaml(
            self.profile_path,
            malformed_profile,
        )

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Root validation",
            result.stdout,
        )

        self.assertIn(
            "missing the 'metarci_profile' root",
            result.stdout,
        )

    def test_missing_record_root_fails(self) -> None:
        """The record document must use metarci_record."""
        record = self.load_yaml(self.record_path)

        malformed_record = {
            "wrong_root": record["metarci_record"],
        }

        self.save_yaml(
            self.record_path,
            malformed_record,
        )

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "Root validation",
            result.stdout,
        )

        self.assertIn(
            "missing the 'metarci_record' root",
            result.stdout,
        )

    def test_malformed_yaml_fails(self) -> None:
        """Syntactically invalid YAML should fail during loading."""
        self.record_path.write_text(
            (
                "metarci_record:\n"
                "  profile: ../profiles/example-profile.yaml\n"
                "    profile_version: \"0.1.0\"\n"
            ),
            encoding="utf-8",
        )

        result = self.run_validator()

        self.assertEqual(result.returncode, 1)

        self.assertIn(
            "ERROR:",
            self.combined_output(result),
        )


if __name__ == "__main__":
    unittest.main()