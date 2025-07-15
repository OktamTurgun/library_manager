from utils.helpers import (
    load_books, save_books, validate_year, add_book,
    search_books, delete_book, update_book, sort_books,
    get_book_statistics, export_books_to_csv
)
import unittest
import json
import os
import tempfile
import shutil
from unittest.mock import patch, mock_open
from datetime import datetime

# Import functions to test
import sys
sys.path.append('..')


class TestHelpers(unittest.TestCase):
    """Test cases for helpers.py functions"""

    def setUp(self):
        """Test uchun ma'lumotlarni tayyorlash"""
        self.test_books = [
            {'title': 'Python Programming', 'author': 'John Smith', 'year': 2020},
            {'title': 'Data Science', 'author': 'Jane Doe', 'year': 2019},
            {'title': 'Machine Learning', 'author': 'John Smith', 'year': 2021}
        ]

        # Test fayl uchun vaqtinchalik papka
        self.test_dir = tempfile.mkdtemp()
        self.test_data_file = os.path.join(self.test_dir, 'test_books.json')

    def tearDown(self):
        """Testdan keyin tozalash"""
        shutil.rmtree(self.test_dir)

    def test_load_books_empty_file(self):
        """Bo'sh fayl yuklashni test qilish"""
        with patch('utils.helpers.DATA_FILE', self.test_data_file):
            result = load_books()
            self.assertEqual(result, [])

    def test_load_books_with_data(self):
        """Ma'lumotlar bilan fayl yuklashni test qilish"""
        # Test ma'lumotlarini yozish
        with open(self.test_data_file, 'w', encoding='utf-8') as f:
            json.dump(self.test_books, f, ensure_ascii=False, indent=4)

        with patch('utils.helpers.DATA_FILE', self.test_data_file):
            result = load_books()
            self.assertEqual(result, self.test_books)

    def test_load_books_file_error(self):
        """Fayl xatosi bilan yuklashni test qilish"""
        with patch('utils.helpers.DATA_FILE', '/nonexistent/file.json'):
            result = load_books()
            self.assertEqual(result, [])

    def test_save_books_success(self):
        """Kitoblarni saqlashni test qilish"""
        with patch('utils.helpers.DATA_FILE', self.test_data_file):
            result = save_books(self.test_books)
            self.assertTrue(result)

            # Saqlangan ma'lumotlarni tekshirish
            with open(self.test_data_file, 'r', encoding='utf-8') as f:
                saved_data = json.load(f)
            self.assertEqual(saved_data, self.test_books)

    def test_validate_year_valid(self):
        """To'g'ri yilni test qilish"""
        current_year = datetime.now().year
        self.assertTrue(validate_year(str(current_year)))
        self.assertTrue(validate_year('2020'))
        self.assertTrue(validate_year('1000'))

    def test_validate_year_invalid(self):
        """Noto'g'ri yilni test qilish"""
        self.assertFalse(validate_year('abc'))
        self.assertFalse(validate_year('999'))
        self.assertFalse(validate_year('3000'))
        self.assertFalse(validate_year(''))

    def test_add_book_success(self):
        """Kitob qo'shishni test qilish"""
        books = []
        with patch('utils.helpers.save_books', return_value=True):
            result = add_book(books, 'New Book', 'New Author', '2023')
            self.assertTrue(result)
            self.assertEqual(len(books), 1)
            self.assertEqual(books[0]['title'], 'New Book')
            self.assertEqual(books[0]['author'], 'New Author')
            self.assertEqual(books[0]['year'], 2023)

    def test_add_book_empty_fields(self):
        """Bo'sh maydonlar bilan kitob qo'shishni test qilish"""
        books = []
        result = add_book(books, '', 'Author', '2023')
        self.assertFalse(result)

        result = add_book(books, 'Title', '', '2023')
        self.assertFalse(result)

    def test_add_book_invalid_year(self):
        """Noto'g'ri yil bilan kitob qo'shishni test qilish"""
        books = []
        result = add_book(books, 'Title', 'Author', 'abc')
        self.assertFalse(result)

    def test_add_book_duplicate(self):
        """Duplikat kitob qo'shishni test qilish"""
        books = [{'title': 'Existing Book', 'author': 'Author', 'year': 2020}]
        result = add_book(books, 'Existing Book', 'Author', '2023')
        self.assertFalse(result)

    def test_search_books_found(self):
        """Kitob qidirishni test qilish - topildi"""
        results = search_books(self.test_books, 'Python')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], 'Python Programming')

    def test_search_books_not_found(self):
        """Kitob qidirishni test qilish - topilmadi"""
        results = search_books(self.test_books, 'Nonexistent')
        self.assertEqual(len(results), 0)

    def test_search_books_empty_keyword(self):
        """Bo'sh kalit so'z bilan qidirishni test qilish"""
        results = search_books(self.test_books, '')
        self.assertEqual(results, self.test_books)

    def test_search_books_case_insensitive(self):
        """Katta-kichik harflarni hisobga olmaslikni test qilish"""
        results = search_books(self.test_books, 'python')
        self.assertEqual(len(results), 1)

    def test_delete_book_success(self):
        """Kitob o'chirishni test qilish - muvaffaqiy"""
        books = self.test_books.copy()
        with patch('utils.helpers.save_books', return_value=True):
            result = delete_book(books, 'Python Programming')
            self.assertTrue(result)
            self.assertEqual(len(books), 2)

    def test_delete_book_not_found(self):
        """Kitob o'chirishni test qilish - topilmadi"""
        books = self.test_books.copy()
        with patch('utils.helpers.save_books', return_value=True):
            result = delete_book(books, 'Nonexistent Book')
            self.assertFalse(result)
            self.assertEqual(len(books), 3)

    def test_update_book_success(self):
        """Kitob yangilashni test qilish - muvaffaqiy"""
        books = self.test_books.copy()
        with patch('utils.helpers.save_books', return_value=True):
            result = update_book(books, 'Python Programming',
                                 'New Title', 'New Author', '2023')
            self.assertTrue(result)
            updated_book = next(b for b in books if b['title'] == 'New Title')
            self.assertEqual(updated_book['author'], 'New Author')
            self.assertEqual(updated_book['year'], 2023)

    def test_update_book_not_found(self):
        """Kitob yangilashni test qilish - topilmadi"""
        books = self.test_books.copy()
        result = update_book(books, 'Nonexistent Book',
                             'New Title', 'New Author', '2023')
        self.assertFalse(result)

    def test_update_book_invalid_year(self):
        """Noto'g'ri yil bilan yangilashni test qilish"""
        books = self.test_books.copy()
        result = update_book(books, 'Python Programming',
                             'New Title', 'New Author', 'abc')
        self.assertFalse(result)

    def test_sort_books_by_title(self):
        """Kitoblarni nomi bo'yicha saralashni test qilish"""
        sorted_books = sort_books(self.test_books, 'title')
        self.assertEqual(sorted_books[0]['title'], 'Data Science')
        self.assertEqual(sorted_books[1]['title'], 'Machine Learning')
        self.assertEqual(sorted_books[2]['title'], 'Python Programming')

    def test_sort_books_by_author(self):
        """Kitoblarni muallifi bo'yicha saralashni test qilish"""
        sorted_books = sort_books(self.test_books, 'author')
        self.assertEqual(sorted_books[0]['author'], 'Jane Doe')
        self.assertEqual(sorted_books[1]['author'], 'John Smith')

    def test_sort_books_by_year(self):
        """Kitoblarni yili bo'yicha saralashni test qilish"""
        sorted_books = sort_books(self.test_books, 'year')
        self.assertEqual(sorted_books[0]['year'], 2019)
        self.assertEqual(sorted_books[1]['year'], 2020)
        self.assertEqual(sorted_books[2]['year'], 2021)

    def test_sort_books_invalid_key(self):
        """Noto'g'ri kalit bilan saralashni test qilish"""
        sorted_books = sort_books(self.test_books, 'invalid_key')
        self.assertEqual(sorted_books, self.test_books)

    def test_get_book_statistics_empty(self):
        """Bo'sh ro'yxat statistikasini test qilish"""
        stats = get_book_statistics([])
        self.assertEqual(stats['total_books'], 0)
        self.assertEqual(stats['authors_count'], 0)
        self.assertIsNone(stats['years_range'])
        self.assertIsNone(stats['most_common_author'])

    def test_get_book_statistics_with_data(self):
        """Ma'lumotlar bilan statistikani test qilish"""
        stats = get_book_statistics(self.test_books)
        self.assertEqual(stats['total_books'], 3)
        self.assertEqual(stats['authors_count'], 2)
        self.assertEqual(stats['years_range'], (2019, 2021))
        self.assertEqual(stats['most_common_author'], 'John Smith')

    def test_export_books_to_csv_success(self):
        """CSV eksportni test qilish - muvaffaqiy"""
        csv_file = os.path.join(self.test_dir, 'test_export.csv')
        result = export_books_to_csv(self.test_books, csv_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(csv_file))

        # CSV fayl mazmunini tekshirish
        with open(csv_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn('title,author,year', content)
            self.assertIn('Python Programming,John Smith,2020', content)

    def test_export_books_to_csv_error(self):
        """CSV eksportni test qilish - xatolik"""
        # Noto'g'ri papka
        result = export_books_to_csv(self.test_books, '/invalid/path/test.csv')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
