from flask import (
    Flask,
    request,
    redirect,
    url_for,
    session,
    flash,
    render_template_string,
)
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "goiteens"


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()


base_template = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul style="color: red;">
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    {{ body | safe }}
</body>
</html>
"""


@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("notes"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password),
            )
            conn.commit()
            conn.close()
            flash("Реєстрація успішна, увійдіть у свій акаунт.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            conn.close()
            flash("Користувач з таким ім'ям вже існує. Спробуйте інше ім'я.")
            return redirect(url_for("register"))
    body = """
        <h2>Реєстрація</h2>
        <form method="post">
            Ім'я користувача: <input type="text" name="username"><br>
            Пароль: <input type="password" name="password"><br>
            <input type="submit" value="Зареєструватися">
        </form>
        <br>
        <a href="/login">Вже маєте акаунт? Увійдіть</a>
    """
    return render_template_string(base_template, title="Реєстрація", body=body)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            flash("Вхід успішний!")
            return redirect(url_for("notes"))
        else:
            flash("Невірне ім'я користувача або пароль.")
            return redirect(url_for("login"))
    body = """
        <h2>Вхід</h2>
        <form method="post">
            Ім'я користувача: <input type="text" name="username"><br>
            Пароль: <input type="password" name="password"><br>
            <input type="submit" value="Увійти">
        </form>
        <br>
        <a href="/register">Немає акаунту? Зареєструйтесь</a>
    """
    return render_template_string(base_template, title="Вхід", body=body)


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    flash("Ви вийшли з акаунту.")
    return redirect(url_for("login"))


@app.route("/notes", methods=["GET", "POST"])
def notes():
    if "user_id" not in session:
        flash("Будь ласка, увійдіть у систему.")
        return redirect(url_for("login"))
    conn = get_db_connection()
    if request.method == "POST":
        content = request.form["content"]
        user_id = session["user_id"]
        conn.execute(
            "INSERT INTO notes (user_id, content) VALUES (?, ?)", (user_id, content)
        )
        conn.commit()
    user_notes = conn.execute(
        "SELECT * FROM notes WHERE user_id = ?", (session["user_id"],)
    ).fetchall()
    conn.close()
    body = "<h2>Ваші нотатки</h2>"
    body += """
        <form method="post">
            Нова нотатка: <input type="text" name="content">
            <input type="submit" value="Додати нотатку">
        </form><br>
    """
    for note in user_notes:
        body += f"<p>{note['content']}</p>"
    body += '<br><a href="/logout">Вийти</a>'
    return render_template_string(base_template, title="Нотатки", body=body)


if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
