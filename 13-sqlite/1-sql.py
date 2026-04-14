import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")
conn.commit()

cursor.execute("""
INSERT INTO books (title, author, year)
VALUES
    ('Harry Potter and the Goblet of Fire', 'J.K. Rowling', 2000),
    ('The Da Vinci Code', 'Dan Brown', 2003),
    ('The Road', 'Cormac McCarthy', 2006),
    ('','','1000')
""")
conn.commit()

               
cursor.execute("SELECT author, year FROM books WHERE year >= 2003")

for book in cursor.fetchall():
    print(book)


conn.close()
