from flask import Flask, make_response, request

app = Flask(__name__)

# 1. Отримати печеньку 🍪
@app.route("/cookie")
def get_cookie():
    resp = make_response("""
        <h1>🍪 Ти отримав печеньку!</h1>
        <a href="/">Перевірити печеньку</a>
    """)

    resp.set_cookie("cookie", "chocolate")

    return resp


# 2. Перевірити печеньку
@app.route("/")
def check_cookie():
    cookie = request.cookies.get("cookie")

    if cookie:
        return f"""
            <h1>✅ Печенька є!</h1>
            <p>Тип: {cookie}</p>
            <a href="/cookie">Отримати ще</a>
        """
    else:
        return """
            <h1>❌ Печеньки немає</h1>
            <a href="/cookie">Отримати печеньку</a>
        """


if __name__ == "__main__":
    app.run(debug=True)