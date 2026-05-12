import sqlite3
from flask import Flask, g, render_template, request

app = Flask(__name__)

DATABASE = 'sql-database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    password TEXT NOT NULL,
                    age INTEGER,
                    city TEXT NOT NULL
                    )""")
    db.commit()

def add_users():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("INSERT INTO users (name, password, age, city) VALUES (?, ?, ?, ?)", ("Олег", "pass123", 25, "Київ"))

    cursor.execute("INSERT INTO users (name, password, age, city) VALUES (?, ?, ?, ?)", ("Марія", "secure456", 30, "Львів"))

    cursor.execute("INSERT INTO users (name, password, age, city) VALUES (?, ?, ?, ?)", ("Іван", "qwerty789", 22, "Одеса"))

    db.commit()
    db.close()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        
        conn = get_db()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE name = ? AND password = ?"
        cursor.execute(query, [username, password])
        user = cursor.fetchone()

        if user:
            return "Успішний вхід!"
        else:
            return "Невірні дані!"

    return '''
        <form method="post">
            <input type="text" name="name" placeholder="Username"><br>
            <input type="password" name="password" placeholder="Password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    with app.app_context():
        create_table()
        add_users()
        app.run(debug=True)