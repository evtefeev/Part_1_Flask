from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    UserMixin,
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)


app = Flask(__name__)
app.secret_key = "goiteens"

login_manager = LoginManager()
login_manager.init_app(app)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = str(id)
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        if user is None:
            return None
        return User(user["id"], user["username"], user["password"])

    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()
        if user is None:
            return None
        return User(user["id"], user["username"], user["password"])


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.find_by_username(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Вхід успішний!")
            return redirect(url_for("dashboard"))
        else:
            flash("Невірне ім'я користувача або пароль.")
            return redirect(url_for("login"))
    return render_template("login.html", title="Вхід")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed = generate_password_hash(password)
        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed),
            )
            conn.commit()
            conn.close()
            flash("Реєстрація успішна, увійдіть у свій акаунт.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            conn.close()
            flash("Користувач з таким ім'ям вже існує. Спробуйте інше ім'я.")
            return redirect(url_for("register"))
    return render_template("register.html", title="Реєстрація")


@app.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html", title="Dashboard", current_user=current_user
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Ви вийшли з акаунту.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
