# Asosiy file
from utils.helpers import *


def show_books(books):
    if not books:
        print("📚 Hech qanday kitob yo'q.")
        return
    for book in books:
        print(f"{book['title']} - {book['author']} ({book['year']})")


def menu():
    books = load_books()
    while True:
        print("""
📚 Kutubxona Menejeri
1 Kitoblarni ko'rish
2 Kitob qo'shish
3 Kitob qidirish
4 Kitob o'chirish
5 Kitonni yangilash
5 Kitoblarni tartiblash
0 Chiqish
      """)

        choice = input("Tanlang: ")

        if choice == '1':
            show_books(books)
        elif choice == '2':
            title = input("Kitob nomi: ")
            author = input("Kitob muallifi: ")
            year = input("Nashr qilingan yili: ")
            if not validate_year(year):
                print("🚫 Yil raqam bo‘lishi kerak.")
                continue
            add_books(books, title, author, year)
            books = load_books()
            print("✅ Kitob qo'shildi")
        elif choice == '3':
            keyword = input("Qidiruv: ")
            results = search_books(books, keyword)
            show_books(results)

        elif choice == '4':
            title = input("O'chirish uchun kitob nomi: ")
            books = delete_books(books, title)
            print("✅ Kitob o‘chirildi.")

        elif choice == '5':
            old_title = input("Qaysi kitobni yangilaysiz (eski nomi): ")
            new_title = input("Yangi nom: ")
            new_author = input("Yangi muallif: ")
            new_year = input("Yangi yil: ")
            if not validate_year(new_year):
                print("🚫 Yil raqam bo‘lishi kerak.")
                continue
            update_book(books, old_title, new_title, new_author, new_year)
            books = load_books()
            print("✅ Kitob yangilandi.")
        elif choice == '6':
            key = input("Nima bo‘yicha? (title/year): ").strip()
            books = sort_books(books, key)
            show_books(books)
        elif choice == '0':
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("🚫 Noto‘g‘ri tanlov.")


if __name__ == "__main__":
    menu()


'''
def menu():
    books = load_books()
    while True:
        print("""
📚 Kutubxona Menejeri
1️⃣ Kitoblarni ko‘rish
2️⃣ Kitob qo‘shish
3️⃣ Kitob qidirish
4️⃣ Kitobni o‘chirish
5️⃣ Kitobni yangilash
6️⃣ Kitoblarni tartiblash
0️⃣ Chiqish
        """)
        choice = input("Tanlang: ")

        if choice == '1':
            show_books(books)
        elif choice == '2':
            title = input("Kitob nomi: ")
            author = input("Muallif: ")
            year = input("Yil: ")
            if not validate_year(year):
                print("🚫 Yil raqam bo‘lishi kerak.")
                continue
            add_book(books, title, author, year)
            books = load_books()
            print("✅ Kitob qo‘shildi.")
        elif choice == '3':
            keyword = input("Qidiruv: ")
            results = search_books(books, keyword)
            show_books(results)
        elif choice == '4':
            title = input("O‘chirish uchun kitob nomi: ")
            books = delete_book(books, title)
            print("✅ Kitob o‘chirildi.")
        elif choice == '5':
            old_title = input("Qaysi kitobni yangilaysiz (eski nomi): ")
            new_title = input("Yangi nom: ")
            new_author = input("Yangi muallif: ")
            new_year = input("Yangi yil: ")
            if not validate_year(new_year):
                print("🚫 Yil raqam bo‘lishi kerak.")
                continue
            update_book(books, old_title, new_title, new_author, new_year)
            books = load_books()
            print("✅ Kitob yangilandi.")
        elif choice == '6':
            key = input("Nima bo‘yicha? (title/year): ").strip()
            books = sort_books(books, key)
            show_books(books)
        elif choice == '0':
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("🚫 Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    menu()
'''
