from flask import Flask, request, make_response, g
import secrets
import html

app = Flask(__name__)

app.secret_key = "secret"

@app.before_request
def generate_nonce():
    g.csp_nonce = secrets.token_urlsafe(16)

@app.after_request
def apply_csp(response):
    response.headers["Content-Security-Policy"] = (
        f"default-src 'self'; "
        f"script-src 'self' 'nonce-{g.csp_nonce}'; "
        f"style-src 'self'; "
        f"frame-ancestors 'none'; "
        f"base-uri 'self'; "
        f"form-action 'self'; "
        f"object-src 'none'"
    )
    return response

@app.route('/')
def index():
    user_name = request.args.get('username', '')
    user_code = request.args.get('user_code', '')

    # Экранирование пользовательского ввода
    user_name = html.escape(user_name)
    user_code = html.escape(user_code)

    html_page = f"""
    <html>
        <body>
            <h1>Ласкаво просимо, користувач!</h1>

            <form method="GET">
                <p>Введіть нікнейм</p>
                <input type="text" name="username">

                <p>Введіть свій код доступу:</p>
                <input type="text" name="user_code">

                <input type="submit" value="Надіслати">
            </form>

            <div>Дякуємо! {user_name}</div>

            <button id="btn">press</button>

            <script nonce="{g.csp_nonce}">
                document
                    .getElementById('btn')
                    .addEventListener('click', () => {{
                        alert('click')
                    }})

                alert('Виконання скрипта дозволено')
            </script>
        </body>
    </html>
    """

    return make_response(html_page)

if __name__ == '__main__':
    app.run(port=5000)