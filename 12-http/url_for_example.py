from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Головна сторінка"

@app.route('/profile')
def profile():
    return "Сторінка профілю"

@app.route('/generate_url')
def generate():
    return url_for('profile')  # Генерує URL-адресу до /profile

if __name__ == '__main__':
    app.run(debug=True)
