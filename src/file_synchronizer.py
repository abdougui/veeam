import os
import shutil
import hashlib


class FileSynchronizer:
    def __init__(self, source, replica, logger):
        self.source = source
        self.replica = replica
        self.logger = logger

    @staticmethod
    def calculate_md5(file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def sync(self):
        source_files = set()

        for dirpath, _, filenames in os.walk(self.source):
            for filename in filenames:
                source_path = os.path.join(dirpath, filename)
                replica_path = os.path.join(
                    self.replica, os.path.relpath(source_path, self.source)
                )
                source_files.add(source_path)

                if os.path.exists(replica_path):
                    if self.calculate_md5(source_path) != self.calculate_md5(
                        replica_path
                    ):
                        shutil.copy2(source_path, replica_path)
                        self.logger.log(f"Updated file: {replica_path}")
                else:
                    os.makedirs(os.path.dirname(replica_path), exist_ok=True)
                    shutil.copy2(source_path, replica_path)
                    self.logger.log(f"Copied new file: {replica_path}")

        self._remove_extra_files(source_files)
        self._remove_empty_dirs()

    def _remove_extra_files(self, source_files):
        for dirpath, _, filenames in os.walk(self.replica):
            for filename in filenames:
                replica_path = os.path.join(dirpath, filename)
                source_path = os.path.join(
                    self.source, os.path.relpath(replica_path, self.replica)
                )

                if source_path not in source_files:
                    os.remove(replica_path)
                    self.logger.log(f"Deleted file: {replica_path}")

    def _remove_empty_dirs(self):
        for dirpath, dirnames, _ in os.walk(self.replica, topdown=False):
            if not os.listdir(dirpath):
                os.rmdir(dirpath)
                self.logger.log(f"Deleted empty directory: {dirpath}")
