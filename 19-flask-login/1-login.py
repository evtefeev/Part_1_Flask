from flask import Flask, session, redirect, url_for, request
# import uuid

app = Flask(__name__)
# key = uuid.uuid4()
app.secret_key = "6da44f9b-396f-41dd-8a66-a324ab6e9cea"
# print(app.secret_key)


@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return f'Ви ввійшли як {username}. <br><a href="/logout">Вийти</a>'
    return 'Ви не увійшли в систему. <br><a href="/login">Увійти</a>'


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return """
        <form method="post">
            Ім'я користувача: <input type="text" name="username">
            <input type="submit" value="Увійти">
        </form>
    """


@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("/"))


if __name__ == "__main__":
    app.run(debug=True)
