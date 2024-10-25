import unittest
from unittest.mock import patch
from src.config import Config
from src.sync_service import SyncService


class TestSyncService(unittest.TestCase):
    @patch("src.sync_service.FileSynchronizer.sync")
    def test_periodic_sync(self, mock_sync):
        mock_config = Config()
        mock_config.source = "test_source"
        mock_config.replica = "test_replica"
        mock_config.interval = 1
        mock_config.log_file = "test_log.log"
        sync_service = SyncService(mock_config)
        with patch("time.sleep", return_value=None):
            sync_service.start()
            self.assertTrue(mock_sync.called)


if __name__ == "__main__":
    unittest.main()
