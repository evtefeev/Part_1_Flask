from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return "GET method"
    elif request.method == 'POST':
        return "POST method"


@app.route('/search')
def search():
    query = request.args.get('q')  # Отримуємо параметр "q" з URL
    return f"Ви шукали: {query}"

if __name__ == '__main__':
    app.run(debug=True)
