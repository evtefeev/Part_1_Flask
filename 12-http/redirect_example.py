from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Головна сторінка!"

@app.route('/login')
def login():
    return "Сторінка входу!"

@app.route('/random')
def redirect_to_login():
    return redirect(url_for('login'))  # Перенаправлення на /login

if __name__ == '__main__':
    app.run(debug=True)