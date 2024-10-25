import unittest
import os
import shutil
from src.file_synchronizer import FileSynchronizer
from src.logger import Logger


class TestFileSynchronizer(unittest.TestCase):
    def setUp(self):
        self.source_dir = "test_source"
        self.replica_dir = "test_replica"
        self.log_file = "test_sync_log.log"
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

    def test_copy_new_file(self):
        test_file = os.path.join(self.source_dir, "new_file.txt")
        with open(test_file, "w") as f:
            f.write("New file content")
        self.synchronizer.sync()
        replica_file = os.path.join(self.replica_dir, "new_file.txt")
        self.assertTrue(os.path.exists(replica_file))

    def test_delete_extra_file(self):
        extra_file = os.path.join(self.replica_dir, "extra_file.txt")
        with open(extra_file, "w") as f:
            f.write("Extra file content")
        self.synchronizer.sync()
        self.assertFalse(os.path.exists(extra_file))


if __name__ == "__main__":
    unittest.main()
