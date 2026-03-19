import unittest
from lab10 import NotificationService, UserManager
from unittest.mock import MagicMock

class TestUserManager(unittest.TestCase):
    def test_notify_user_calls_send(self):
        mock_service = MagicMock(spec=NotificationService)
        user_manager = UserManager(mock_service)
        user_manager.notify_user("Yuliia", "Wassap")
        mock_service.send.assert_called_once()
        expected_message = "Hello, Yuliia! Wassap"
        mock_service.send.assert_called_with(expected_message)

if __name__ == '__main__':
    unittest.main()
