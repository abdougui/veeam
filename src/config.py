import argparse
import os


class Config:
    def __init__(self):
        self.source, self.replica, self.interval, self.log_file = self.parse_args()

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="Folder Synchronizer")
        parser.add_argument("source", help="Source folder path")
        parser.add_argument("replica", help="Replica folder path")
        parser.add_argument("interval", type=int, help="Sync interval in seconds")
        parser.add_argument("log_file", help="Log file path")
        args = parser.parse_args()

        if not os.path.isdir(args.source):
            raise ValueError("Source folder does not exist.")
        if not os.path.isdir(args.replica):
            raise ValueError("Replica folder does not exist.")

        return args.source, args.replica, args.interval, args.log_file
