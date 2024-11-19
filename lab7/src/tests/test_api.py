import unittest
from unittest.mock import patch, MagicMock
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from src.bll.classes.api.ApiHandler import APIHandler
from src.bll.classes.api.user_repository import UserRepository

class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        self.api_handler = APIHandler()

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": 1, "name": "Test User"}]

        result = self.api_handler.get_data("users")
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["name"], "Test User")

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"error": "Not Found"}

        result = self.api_handler.get_data("unknown")
        self.assertEqual(result, {"error": "Not Found"})


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.api_handler = MagicMock()
        self.user_repo = UserRepository(self.api_handler)

    def test_get_users(self):
        self.api_handler.get_data.return_value = [{"id": 1, "name": "Test User"}]

        users = self.user_repo.get_users()
        self.api_handler.get_data.assert_called_once_with("users")
        self.assertEqual(users[0]["id"], 1)
        self.assertEqual(users[0]["name"], "Test User")

    def test_get_posts(self):
        self.api_handler.get_data.return_value = [{"id": 1, "title": "Test Post"}]

        posts = self.user_repo.get_posts()
        self.api_handler.get_data.assert_called_once_with("posts")
        self.assertEqual(posts[0]["id"], 1)
        self.assertEqual(posts[0]["title"], "Test Post")


if __name__ == "__main__":
    unittest.main()
