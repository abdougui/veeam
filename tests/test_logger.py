import unittest
import os
from src.logger import Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_log.log"
        self.logger = Logger(self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_message(self):
        message = "Test log message"
        self.logger.log(message)
        with open(self.log_file, "r") as log:
            log_content = log.read()
            self.assertIn(message, log_content)


if __name__ == "__main__":
    unittest.main()
