import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class RepoShapeTests(unittest.TestCase):
    def test_nested_repo_exists(self):
        self.assertTrue((ROOT / "services" / "api").exists())

    def test_migration_and_rollback_present(self):
        migration_dir = ROOT / "migrations"
        self.assertTrue((migration_dir / "0003_add_automation_tables.sql").exists())
        self.assertTrue((migration_dir / "0003_rollback_automation.sql").exists())

if __name__ == "__main__":
    unittest.main()
