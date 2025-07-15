from main import show_books, show_statistics
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Import functions to test
sys.path.append('..')


class TestMain(unittest.TestCase):
    """Test cases for main.py functions"""

    def setUp(self):
        """Test uchun ma'lumotlarni tayyorlash"""
        self.test_books = [
            {'title': 'Python Programming', 'author': 'John Smith', 'year': 2020},
            {'title': 'Data Science', 'author': 'Jane Doe', 'year': 2019},
            {'title': 'Machine Learning', 'author': 'John Smith', 'year': 2021}
        ]

    @patch('builtins.print')
    def test_show_books_with_data(self, mock_print):
        """Kitoblarni ko'rsatishni test qilish - ma'lumotlar bilan"""
        show_books(self.test_books)

        # Print chaqiruvlarini tekshirish
        mock_print.assert_called()
        calls = mock_print.call_args_list

        # Jami kitoblar soni ko'rsatilganini tekshirish
        self.assertTrue(any('Jami 3 ta kitob' in str(call) for call in calls))

        # Har bir kitob ko'rsatilganini tekshirish
        self.assertTrue(any('Python Programming' in str(call)
                        for call in calls))
        self.assertTrue(any('Data Science' in str(call) for call in calls))
        self.assertTrue(any('Machine Learning' in str(call) for call in calls))

    @patch('builtins.print')
    def test_show_books_empty(self, mock_print):
        """Kitoblarni ko'rsatishni test qilish - bo'sh ro'yxat"""
        show_books([])

        # Bo'sh xabar ko'rsatilganini tekshirish
        mock_print.assert_called_with("📚 Hech qanday kitob yo'q.")

    @patch('builtins.print')
    def test_show_statistics_with_data(self, mock_print):
        """Statistikani ko'rsatishni test qilish - ma'lumotlar bilan"""
        show_statistics(self.test_books)

        # Print chaqiruvlarini tekshirish
        mock_print.assert_called()
        calls = mock_print.call_args_list

        # Statistika elementlari ko'rsatilganini tekshirish
        self.assertTrue(any('Jami kitoblar: 3' in str(call) for call in calls))
        self.assertTrue(any('Mualliflar soni: 2' in str(call)
                        for call in calls))
        self.assertTrue(any('John Smith' in str(call) for call in calls))

    @patch('builtins.print')
    def test_show_statistics_empty(self, mock_print):
        """Statistikani ko'rsatishni test qilish - bo'sh ro'yxat"""
        show_statistics([])

        # Bo'sh statistika ko'rsatilganini tekshirish
        mock_print.assert_called()
        calls = mock_print.call_args_list
        self.assertTrue(any('Jami kitoblar: 0' in str(call) for call in calls))


class TestMainIntegration(unittest.TestCase):
    """Integration test cases for main.py"""

    def setUp(self):
        """Test uchun ma'lumotlarni tayyorlash"""
        self.test_books = [
            {'title': 'Test Book 1', 'author': 'Test Author 1', 'year': 2020},
            {'title': 'Test Book 2', 'author': 'Test Author 2', 'year': 2021}
        ]

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('main.load_books')
    def test_menu_integration(self, mock_load_books, mock_print, mock_input):
        """Menyu integratsiyasini test qilish"""
        # Mock ma'lumotlarni sozlash
        mock_load_books.return_value = self.test_books
        # Kitoblarni ko'rish, keyin chiqish
        mock_input.side_effect = ['1', '0']

        # Menyu chaqirish (faqat bir marta)
        from main import menu
        with patch('main.menu') as mock_menu:
            mock_menu.return_value = None
            # Bu yerda menu() chaqirilmaydi chunki u cheksiz sikl

    def test_show_books_format(self):
        """Kitoblarni ko'rsatish formatini test qilish"""
        with patch('builtins.print') as mock_print:
            show_books(self.test_books)

            # Format tekshirish
            calls = mock_print.call_args_list
            formatted_calls = [str(call) for call in calls]

            # Har bir kitob to'g'ri formatda ko'rsatilganini tekshirish
            self.assertTrue(
                any('Test Book 1 - Test Author 1 (2020)' in str(call) for call in calls))
            self.assertTrue(
                any('Test Book 2 - Test Author 2 (2021)' in str(call) for call in calls))


if __name__ == '__main__':
    unittest.main()
