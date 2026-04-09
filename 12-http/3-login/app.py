from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']  # Отримуємо ім'я з форми
        return f'Запит методом POST, введене ім\'я: {user}'
    else:
        return render_template('login.html')  # Відображаємо форму для введення

if __name__ == '__main__':
    app.run(debug=True)
