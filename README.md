
# 📚 Library Manager

Python asosida yozilgan oddiy, lekin kengaytirilgan kutubxona boshqaruv dasturi.

---

## ✨ Xususiyatlar
✅ Kitoblarni ko'rish  
✅ Kitob qo'shish (yil validatsiyasi bilan)  
✅ Kitobni qidirish (nom yoki muallif bo'yicha)  
✅ Kitobni o'chirish  
✅ Kitobni yangilash  
✅ Kitoblarni tartiblash (nom, muallif yoki yil bo'yicha)  
✅ Kitoblar statistikasi  
✅ CSV formatda eksport qilish  
✅ Ma'lumotlarni `books.json` ga saqlash va yuklash  
✅ Xatoliklarni qayta ishlash  
✅ Type hints va dokumentatsiya  

---

## 📘 Maydonlar
| Maydon     | Tavsif              |
|------------|--------------------|
| `title`    | Kitob nomi         |
| `author`   | Kitob muallifi     |
| `year`     | Noshir yili (raqam)|

---

## 🛠️ Texnologiyalar
- Python 3.x
- `json` moduli
- `csv` moduli (eksport uchun)
- `typing` moduli (type hints uchun)
- `datetime` moduli (yil validatsiyasi uchun)
- `unittest` moduli (testlar uchun)
- Fayllar bilan ishlash
- Funksiya, sikl, shart operatorlari
- Modulga ajratilgan kod (`utils/helpers.py`)

---

## 🚀 Ishga tushirish

1️⃣ Reponi klonlash:
```bash
git clone https://github.com/username/library-manager.git
cd library-manager
```

2️⃣ Dastur ishga tushirish:
```bash
python main.py
```

3️⃣ Testlarni ishga tushirish:
```bash
python run_tests.py
```

---

## 📋 Foydalanish

Dastur ishga tushgandan so'ng quyidagi menyu ko'rinadi:

```
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
```

### Yangi xususiyatlar:

**📊 Statistika (7️⃣):**
- Jami kitoblar soni
- Mualliflar soni
- Yillar oralig'i
- Eng ko'p kitob yozgan muallif

**📁 CSV Eksport (8️⃣):**
- Kitoblarni CSV formatda saqlash
- Boshqa dasturlarda foydalanish uchun

**🔍 Yaxshilangan qidiruv:**
- Bo'sh qidiruv barcha kitoblarni ko'rsatadi
- Natijalar soni ko'rsatiladi

---

## 🧪 Testlar

Loyiha keng qamrovli testlar bilan ta'minlangan:

### Test tuzilishi:
- `tests/test_helpers.py` - Yordamchi funksiyalar testlari
- `tests/test_main.py` - Asosiy funksiyalar testlari
- `run_tests.py` - Test ishga tushiruvchi

### Test qamrovi:
- ✅ Fayl o'qish/yozish operatsiyalari
- ✅ Ma'lumotlar validatsiyasi
- ✅ Kitob qo'shish/o'chirish/yangilash
- ✅ Qidiruv va saralash funksiyalari
- ✅ Statistika hisoblash
- ✅ CSV eksport
- ✅ Xatoliklar bilan ishlash

### Test natijalari:
```bash
📊 Test natijalari:
   ✅ Muvaffaqiy: 25
   ❌ Xatoliklar: 0
   ⚠️  Xatolar: 0
   📊 Jami: 25
```

---

## 📂 Papka tuzilishi
```text
library-manager/
├── main.py              # Asosiy dastur
├── data/
│   └── books.json      # Kitoblar ma'lumotlari
├── utils/
│   └── helpers.py      # Yordamchi funksiyalar
├── tests/
│   ├── __init__.py     # Test paketi
│   ├── test_helpers.py # Helpers funksiyalari testlari
│   └── test_main.py    # Main funksiyalari testlari
├── run_tests.py         # Test ishga tushiruvchi
├── README.md
├── .gitignore
├── LICENSE
```

---

## 🔧 Optimizatsiyalar (2024)

### Xatoliklarni qayta ishlash:
- Fayl o'qish/yozish xatoliklari
- JSON format xatoliklari
- Ma'lumotlar validatsiyasi

### Yangi funksiyalar:
- `get_book_statistics()` - statistika hisoblash
- `export_books_to_csv()` - CSV eksport
- Yaxshilangan `validate_year()` - yil tekshirish
- `run_tests.py` - test ishga tushiruvchi

### Kod sifatini oshirish:
- Type hints qo'shildi
- Docstring dokumentatsiyasi
- Input validatsiyasi
- Duplikat tekshirish
- Unit testlar qo'shildi

### Foydalanuvchi interfeysi:
- Yaxshilangan xabar berish
- Xatolik xabarlari
- Natijalar soni ko'rsatish

---

## 👨‍💻 Muallif
💻 OktamTurgun  
🌐 GitHub: [OktamTurgun](https://github.com/OktamTurgun)

---

## 🔗 Loyiha
📂 Repo: [library_manager](https://github.com/OktamTurgun/library_manager)

---

## 📜 Litsenziya
[MIT](LICENSE)
