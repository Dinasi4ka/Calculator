import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from bll.classes.api.utils import display_as_list, display_as_table, log_request
from bll.classes.api.ApiHandler import APIHandler

class TestAPIHandler(unittest.TestCase):
    
    def setUp(self):
        """Створення екземпляра APIHandler перед кожним тестом"""
        self.api = APIHandler()
    
    def test_get_data_valid_endpoint(self):
        """Перевірка успішного отримання даних для коректного ендпоінту"""
        data = self.api.get_data('users')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0, "Expected non-empty data list")
    
    def test_get_data_invalid_endpoint(self):
        """Перевірка обробки помилки для неправильного ендпоінту"""
        data = self.api.get_data('invalid_endpoint')
        self.assertEqual(data, {}, "Expected an empty dictionary for an invalid endpoint")

    @patch('bll.classes.api.utils.get_user_color_choice', return_value="blue")  # Мокаємо функцію вибору кольору
    def test_display_as_table(self, mock_get_color):
        """Перевірка виведення даних у вигляді таблиці без запиту кольору"""
        data = [{'id': 1, 'name': 'Test User', 'email': 'test@example.com'}]
        try:
            display_as_table(data)  # Викликаємо функцію, яка тепер не потребує вибору кольору
        except Exception as e:
            self.fail(f"display_as_table raised an exception {e}")

    def test_display_as_list(self):
        """Перевірка виведення даних у вигляді списку"""
        data = [{'id': 1, 'name': 'Test User', 'email': 'test@example.com'}]
        try:
            display_as_list(data)
        except Exception as e:
            self.fail(f"display_as_list raised an exception {e}")

    def test_edge_case_empty_data(self):
        """Перевірка обробки порожнього списку даних"""
        data = []
        result = display_as_table(data, header_color="blue")  # Вказуємо колір за замовчуванням
        self.assertIsNone(result, "Expected None for empty data list")

    def test_log_request(self):
        """Перевірка логування запиту"""
        endpoint = 'users'
        data = [{'id': 1, 'name': 'Test User'}]
        result = "Data received successfully, displaying as table."
        try:
            log_request("GET", endpoint, data, "table", result)
        except Exception as e:
            self.fail(f"log_request raised an exception {e}")
    
    def test_invalid_display_format(self):
        """Перевірка обробки неправильного формату виводу"""
        with self.assertRaises(ValueError):
            self.api.get_data("users", display_format="invalid_format")
        
if __name__ == "__main__":
    unittest.main()
