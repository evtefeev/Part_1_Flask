from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super_secret_key"  # обов’язково!

# 1. Отримати "печеньку"
@app.route("/get-cookie")
def get_cookie():
    session["cookie"] = "chocolate"

    return """
        <h1>🍪 Ти отримав печеньку!</h1>
        <a href="/check-cookie">Перевірити печеньку</a>
    """


# 2. Перевірити
@app.route("/check-cookie")
def check_cookie():
    cookie = session.get("cookie")

    if cookie:
        return f"""
            <h1>✅ Печенька є!</h1>
            <p>Тип: {cookie}</p>
            <a href="/get-cookie">Отримати ще</a>
        """
    else:
        return """
            <h1>❌ Печеньки немає</h1>
            <a href="/get-cookie">Отримати печеньку</a>
        """


# 3. Видалити (опціонально)
@app.route("/clear")
def clear():
    session.clear()
    return "Session очищена"


if __name__ == "__main__":
    app.run(debug=True)