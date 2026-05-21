from flask import Flask, request, redirect, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "SUPER_SECRET_KEY"

DATABASE = "users.db"


def get_db():
    """Return DB connection tied to current request context"""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Automatically close DB after request"""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Initialize database schema"""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        conn.commit()


with app.app_context():
    init_db()


@app.route("/")
def home():

    if "user" in session:
        return (
            f"""
            <h1>Вітаю, {session["user"]}</h1>
            <a href="/profile">Profile</a><br><br>
            <a href="/logout">Logout</a>
        """,
            200,
        )

    return (
        """
        <h1>Головна сторінка</h1>
        <a href="/login">Login</a><br><br>
        <a href="/register">Register</a>
    """,
        200,
    )


@app.route("/register")
def register_page():
    return (
        """
        <h1>Register</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Username"><br><br>
            <input type="password" name="password" placeholder="Password"><br><br>
            <button>Register</button>
        </form>
    """,
        200,
    )


@app.route("/register", methods=["POST"])
def register():

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "<h1>Bad request</h1>", 400

    if len(password) < 6:
        return "<h1>Password too short</h1>", 400

    hashed_password = generate_password_hash(password)

    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, hashed_password),
        )

        db.commit()

        return redirect("/login"), 302

    except sqlite3.IntegrityError:
        return "<h1>User already exists</h1>", 409


@app.route("/login")
def login_page():
    return (
        """
        <h1>Login</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Username"><br><br>
            <input type="password" name="password" placeholder="Password"><br><br>
            <button>Login</button>
        </form>
    """,
        200,
    )


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))

    user = cursor.fetchone()

    if not user:
        return "<h1>Invalid credentials</h1>", 401

    if not check_password_hash(user["password"], password):
        return "<h1>Invalid credentials</h1>", 401

    session["user"] = username

    return redirect("/"), 302


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/"), 302


@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login"), 302

    return (
        f"""
        <h1>Profile</h1>
        <p>Username: {session["user"]}</p>
        <p>Time: {datetime.now()}</p>
        <a href="/">Home</a>
    """,
        200,
    )


@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "GET":
        return """
        <form method='post'>
        <input type='number' name='n1'>
        <input type='number' name='n2'>
        <button>calc</button>
        </form>
        """
    n1 = int(request.form.get("n1"))
    n2 = int(request.form.get("n2"))

    return f"{n1 + n2}", 200


if __name__ == "__main__":
    app.run(debug=True)
