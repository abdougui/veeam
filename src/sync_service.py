from logger import Logger
from file_synchronizer import FileSynchronizer
import time


class SyncService:
    def __init__(self, config):
        self.config = config
        self.logger = Logger(config.log_file)
        self.synchronizer = FileSynchronizer(config.source, config.replica, self.logger)

    def start(self):
        self.logger.log("Starting synchronization service...")
        while True:
            self.synchronizer.sync()
            time.sleep(self.config.interval)
