# Asosiy file
from utils.helpers import *


def show_books(books):
    """Kitoblarni ko'rsatadi"""
    if not books:
        print("📚 Hech qanday kitob yo'q.")
        return
    print(f"\n📚 Jami {len(books)} ta kitob:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} - {book['author']} ({book['year']})")


def show_statistics(books):
    """Kitoblar statistikasini ko'rsatadi"""
    stats = get_book_statistics(books)
    print(f"\n📊 Statistika:")
    print(f"Jami kitoblar: {stats['total_books']}")
    print(f"Mualliflar soni: {stats['authors_count']}")
    if stats['years_range']:
        print(
            f"Yillar oralig'i: {stats['years_range'][0]} - {stats['years_range'][1]}")
    if stats['most_common_author']:
        print(f"Eng ko'p kitob yozgan muallif: {stats['most_common_author']}")


def menu():
    """Asosiy menyu"""
    books = load_books()
    while True:
        print("""
📚 Kutubxona Menejeri
1️⃣ Kitoblarni ko'rish
2️⃣ Kitob qo'shish
3️⃣ Kitob qidirish
4️⃣ Kitob o'chirish
5️⃣ Kitobni yangilash
6️⃣ Kitoblarni tartiblash
7️⃣ Statistika
8️⃣ CSV ga eksport qilish
0️⃣ Chiqish
        """)

        choice = input("Tanlang: ")

        if choice == '1':
            show_books(books)
        elif choice == '2':
            title = input("Kitob nomi: ")
            author = input("Kitob muallifi: ")
            year = input("Nashr qilingan yili: ")
            if add_book(books, title, author, year):
                books = load_books()
                print("✅ Kitob qo'shildi")
            else:
                print("❌ Kitob qo'shilmadi")
        elif choice == '3':
            keyword = input("Qidiruv so'zi: ")
            results = search_books(books, keyword)
            if results:
                print(f"\n🔍 {len(results)} ta natija topildi:")
                show_books(results)
            else:
                print("🔍 Hech qanday natija topilmadi")
        elif choice == '4':
            title = input("O'chirish uchun kitob nomi: ")
            if delete_book(books, title):
                books = load_books()
                print("✅ Kitob o'chirildi.")
            else:
                print("❌ Kitob o'chirilmadi.")
        elif choice == '5':
            old_title = input("Qaysi kitobni yangilaysiz (eski nomi): ")
            new_title = input("Yangi nom: ")
            new_author = input("Yangi muallif: ")
            new_year = input("Yangi yil: ")
            if update_book(books, old_title, new_title, new_author, new_year):
                books = load_books()
                print("✅ Kitob yangilandi.")
            else:
                print("❌ Kitob yangilanmadi.")
        elif choice == '6':
            print("Saralash bo'yicha tanlang:")
            print("1. Nomi bo'yicha")
            print("2. Muallif bo'yicha")
            print("3. Yili bo'yicha")
            sort_choice = input("Tanlang (1-3): ")
            sort_keys = {'1': 'title', '2': 'author', '3': 'year'}
            if sort_choice in sort_keys:
                sorted_books = sort_books(books, sort_keys[sort_choice])
                show_books(sorted_books)
            else:
                print("❌ Noto'g'ri tanlov")
        elif choice == '7':
            show_statistics(books)
        elif choice == '8':
            filename = input(
                "CSV fayl nomi (default: books_export.csv): ").strip()
            if not filename:
                filename = 'books_export.csv'
            if export_books_to_csv(books, filename):
                print(f"✅ Kitoblar {filename} faylga saqlandi")
            else:
                print("❌ Eksport qilishda xatolik")
        elif choice == '0':
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("🚫 Noto'g'ri tanlov.")


if __name__ == "__main__":
    menu()
