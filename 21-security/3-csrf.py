from flask import Flask, render_template, request, session
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = '#cv)3v7w$*s3fk;5c!@y0?:?№3"9)#'
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'


@app.route('/',methods=['GET','POST'])
def index():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)  # Генерація токена якщо його немає в сесії

    if request.method == 'POST':
        if request.form.get("csrf_token") != session["csrf_token"]:
            return "Запит заблоковано!", 403  # Якщо токен не співпадає з токеном у сесії - запит відхиляється
        user_output = request.form['username']
        transfer = request.form['num']
        return f"Ви надіслали кошти на суму {transfer} користувачу {user_output} ."
    return render_template('csrf_form_check.html', csrf_token=session["csrf_token"])




if __name__ == '__main__':
    app.run(port=8001)