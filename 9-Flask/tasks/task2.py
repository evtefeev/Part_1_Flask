# Завдання 2. 

# Створення базового Flask-додатка для роботи з книгами із трьома маршрутами:

# / — Головна сторінка з привітанням.
# /books/ — Сторінка з переліком ваших улюблених книг.
# /book/<int:id>/ — Сторінка з детальною інформацією про конкретну книгу.


# Додаткові завдання:

# Додайте ще один маршрут /genres/, який повертає список жанрів книг без повторень.
# Додайте динамічний маршрут /genre/<genre_name>/, який повертає список книг у зазначеному жанрі.


from flask import Flask

app = Flask(__name__)

# Дані про книги
books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"}
]

# Головна сторінка
@app.route('/')
def index():
    return "Ласкаво просимо до бібліотеки улюблених книг!"

# Список книг
@app.route('/books/')
def book_list():
    books_list = "\\n".join([f"{book['id']}. {book['title']} — {book['author']}" for book in books])
    return f"Список книг:\\n{books_list}"

# Деталі книги
@app.route('/book/<int:id>/')
def book_detail(id):
    book = next((book for book in books if book["id"] == id), None)
    if book:
        return f"Назва: {book['title']}\\nАвтор: {book['author']}\\nЖанр: {book['genre']}"
    else:
        return "Книга не знайдена", 404

if __name__ == "__main__":
    app.run(debug=True)
