# Bu yerda yordamchi funksiyalar bo'ladi

import json
import os

DATA_FILE = 'data/books.json'


def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_books(books):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def validate_year(year):
    return year.isdigit()


def add_books(books, title, author, year):
    books.append({
        'title': title,
        'author': author,
        'year': year
    })
    save_books(books)


def search_books(books, keyword):
    keyword = keyword.lower()
    return [
        book for book in books
        if keyword in book['title'].lower() or keyword in book['author'].lower()
    ]


def delete_books(books, title):
    books = [b for b in books if b['title'].lower() != title.lower()]
    save_books(books)
    return books


def update_book(books, old_title, new_title, new_author, new_year):
    for book in books:
        if book['title'].lower() == old_title.lower():
            book['title'] = new_title
            book['author'] = new_author
            book['year'] = int(new_year)
            break
        save_books(books)


def sort_books(books, key='title'):
    return sorted(books, key=lambda x: x[key].lower() if isinstance(x[key], str) else x[key])
