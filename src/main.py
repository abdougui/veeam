from config import Config
from sync_service import SyncService

if __name__ == "__main__":
    try:
        config = Config()
        service = SyncService(config)
        service.start()
    except Exception as e:
        print(f"Error: {e}")
