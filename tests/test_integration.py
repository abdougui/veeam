import unittest
import os
import shutil
from src.logger import Logger
from src.file_synchronizer import FileSynchronizer


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.source_dir = "test_source"
        self.replica_dir = "test_replica"
        self.log_file = "test_integration_log.log"
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.replica_dir, exist_ok=True)
        self.logger = Logger(self.log_file)
        self.synchronizer = FileSynchronizer(
            self.source_dir, self.replica_dir, self.logger
        )

    def tearDown(self):
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.replica_dir)
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_full_sync(self):
        with open(os.path.join(self.source_dir, "file1.txt"), "w") as f:
            f.write("Content for file 1")
        with open(os.path.join(self.source_dir, "file2.txt"), "w") as f:
            f.write("Content for file 2")

        self.synchronizer.sync()
        self.assertTrue(os.path.exists(os.path.join(self.replica_dir, "file1.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.replica_dir, "file2.txt")))


if __name__ == "__main__":
    unittest.main()
