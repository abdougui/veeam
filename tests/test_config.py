import unittest
from src.config import Config
from unittest.mock import patch


class TestConfig(unittest.TestCase):
    @patch("argparse._sys.argv", ["main.py", "source", "replica", "10", "log_file.log"])
    def test_valid_arguments(self):
        config = Config()
        self.assertEqual(config.source, "source")
        self.assertEqual(config.replica, "replica")
        self.assertEqual(config.interval, 10)
        self.assertEqual(config.log_file, "log_file.log")

    @patch(
        "argparse._sys.argv",
        ["main.py", "nonexistent_source", "replica", "10", "log_file.log"],
    )
    def test_invalid_source_directory(self):
        with self.assertRaises(ValueError):
            Config()


if __name__ == "__main__":
    unittest.main()
