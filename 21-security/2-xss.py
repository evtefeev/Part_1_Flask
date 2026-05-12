from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    user_name = request.args.get('username', '')
    user_code = request.args.get('user_code', '')

    # Логіка сайту, використання вписаних даних.

    html = f"""
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
        </body>
    </html>
    """
    return html.encode()

if __name__ == '__main__':
    app.run(port=5000)