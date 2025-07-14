# Bu yerda yordamchi funksiyalar bo'ladi

import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime

DATA_FILE = 'data/books.json'


def load_books() -> List[Dict[str, Any]]:
    """Kitoblarni fayldan yuklaydi"""
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Faylni o'qishda xatolik: {e}")
        return []


def save_books(books: List[Dict[str, Any]]) -> bool:
    """Kitoblarni faylga saqlaydi"""
    try:
        # data papkasini yaratish
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"Faylga saqlashda xatolik: {e}")
        return False


def validate_year(year: str) -> bool:
    """Yilni tekshiradi"""
    if not year.isdigit():
        return False
    year_int = int(year)
    current_year = datetime.now().year
    return 1000 <= year_int <= current_year


def add_book(books: List[Dict[str, Any]], title: str, author: str, year: str) -> bool:
    """Yangi kitob qo'shadi"""
    if not title.strip() or not author.strip():
        print("Sarlavha va muallif bo'sh bo'lishi mumkin emas")
        return False

    if not validate_year(year):
        print("Noto'g'ri yil format")
        return False

    # Duplikatni tekshirish
    for book in books:
        if book['title'].lower() == title.lower():
            print("Bu kitob allaqachon mavjud")
            return False

    books.append({
        'title': title.strip(),
        'author': author.strip(),
        'year': int(year)
    })
    return save_books(books)


def search_books(books: List[Dict[str, Any]], keyword: str) -> List[Dict[str, Any]]:
    """Kitoblarni qidiradi"""
    if not keyword.strip():
        return books

    keyword = keyword.lower().strip()
    return [
        book for book in books
        if keyword in book['title'].lower() or keyword in book['author'].lower()
    ]


def delete_book(books: List[Dict[str, Any]], title: str) -> bool:
    """Kitobni o'chiradi"""
    if not title.strip():
        return False

    original_length = len(books)
    books[:] = [b for b in books if b['title'].lower() != title.lower().strip()]

    if len(books) == original_length:
        print("Kitob topilmadi")
        return False

    return save_books(books)


def update_book(books: List[Dict[str, Any]], old_title: str, new_title: str,
                new_author: str, new_year: str) -> bool:
    """Kitobni yangilaydi"""
    if not old_title.strip():
        return False

    if not validate_year(new_year):
        print("Noto'g'ri yil format")
        return False

    for book in books:
        if book['title'].lower() == old_title.lower().strip():
            book['title'] = new_title.strip()
            book['author'] = new_author.strip()
            book['year'] = int(new_year)
            return save_books(books)

    print("Yangilash uchun kitob topilmadi")
    return False


def sort_books(books: List[Dict[str, Any]], key: str = 'title') -> List[Dict[str, Any]]:
    """Kitoblarni saralaydi"""
    if not books:
        return books

    valid_keys = ['title', 'author', 'year']
    if key not in valid_keys:
        print(f"Noto'g'ri kalit. Foydalanish mumkin: {valid_keys}")
        return books

    return sorted(books, key=lambda x: str(x[key]).lower() if isinstance(x[key], (str, int)) else str(x[key]))


def get_book_statistics(books: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Kitoblar statistikasini qaytaradi"""
    if not books:
        return {
            'total_books': 0,
            'authors_count': 0,
            'years_range': None,
            'most_common_author': None
        }

    authors = [book['author'] for book in books]
    years = [book['year'] for book in books]

    # Yillarni int ga o'tkazish
    try:
        years_int = [int(year) if isinstance(year, str)
                     else year for year in years]
    except (ValueError, TypeError):
        years_int = []

    # Eng ko'p kitob yozgan muallif
    author_counts = {}
    for author in authors:
        author_counts[author] = author_counts.get(author, 0) + 1

    most_common_author = max(author_counts.items(), key=lambda x: x[1])[
        0] if author_counts else None

    return {
        'total_books': len(books),
        'authors_count': len(set(authors)),
        'years_range': (min(years_int), max(years_int)) if years_int else None,
        'most_common_author': most_common_author
    }


def export_books_to_csv(books: List[Dict[str, Any]], filename: str = 'books_export.csv') -> bool:
    """Kitoblarni CSV formatda eksport qiladi"""
    try:
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'author', 'year']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for book in books:
                writer.writerow(book)
        return True
    except IOError as e:
        print(f"CSV faylga saqlashda xatolik: {e}")
        return False
