# Folder Synchronizer

## Overview

This Folder Synchronizer program maintains a one-way synchronization between two directories: `source` and `replica`. The program makes `replica` a full, identical copy of `source`, ensuring that any additions, modifications, or deletions in `source` are reflected in `replica`.

The synchronization runs periodically, and each operation is logged to both a log file and the console.

## Features

- **One-way Synchronization**: Updates `replica` to mirror `source`.
- **Periodic Syncing**: Synchronization runs at specified intervals.
- **Logging**: Logs file creation, updates, and deletions to both console and file.
- **Configurable**: Folder paths, sync interval, and log file path are provided through command-line arguments.

## Project Structure

```plaintext
project_root/
├── src/
│   ├── main.py               # Main entry point for the sync service
│   ├── config.py             # Config class to handle arguments
│   ├── logger.py             # Logger class for handling logs
│   ├── synchronizer.py       # FileSynchronizer class for core sync logic
│   └── sync_service.py       # SyncService class for managing periodic syncs
├── tests/                    # Contains all test files for the project
├── source/                   # Source directory (user-defined, example)
├── replica/                  # Replica directory (user-defined, example)
└── README.md                 # Project overview and instructions
```

## Requirements

This project uses Python 3.11.5 or higher. To set up the environment and install dependencies, follow these steps:

1. **Install Python**: Ensure Python 3.11.5 or later is installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up Virtual Environment** (recommended):
   - In the project root directory, run:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - **On Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **On macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

## Running the Program

To run the synchronization service, use the following command:

```bash
python src/main.py <source_folder> <replica_folder> <interval> <log_file>
```

### Explanation of Command-Line Arguments

- `<source_folder>`: Path to the source folder to be mirrored.
- `<replica_folder>`: Path to the replica folder where changes will be synced.
- `<interval>`: Time interval in seconds between each synchronization.
- `<log_file>`: Path to the log file where synchronization actions will be recorded.

### Example Run

Here’s an example to illustrate:

```bash
python src/main.py ./source ./replica 10 ./sync_log.log
```

This command will:
1. Take `./source` as the source directory to be mirrored.
2. Use `./replica` as the destination that will mirror `source`.
3. Run the synchronization every 10 seconds.
4. Log all actions to `./sync_log.log`.

**Note**: Ensure both `source` and `replica` directories exist before running the command, as the program does not create directories.

### Stopping the Program

The program will run indefinitely with periodic synchronization every `<interval>` seconds. To stop the program, use `Ctrl + C` in the terminal where the program is running.

## Testing

To run unit tests and integration tests, navigate to the project root and execute:

```bash
pytest tests/
```

or

```bash
python -m unittest discover -s tests
```

## Implementation Details

- **Config Class (`config.py`)**: Handles argument parsing and validation.
- **Logger Class (`logger.py`)**: Manages logging of operations to console and file.
- **FileSynchronizer Class (`file_synchronizer.py`)**: Performs the core synchronization tasks, including copying, updating, and deleting files in the replica.
- **SyncService Class (`sync_service.py`)**: Manages periodic synchronization by invoking `FileSynchronizer` at the specified interval.