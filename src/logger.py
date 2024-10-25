from datetime import datetime


class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"{timestamp} - {message}"

        print(full_message)

        with open(self.log_file, "a") as logf:
            logf.write(full_message + "\n")
