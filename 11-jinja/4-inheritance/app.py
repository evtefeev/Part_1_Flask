from flask import Flask, render_template

app = Flask(__name__)

# Дані про студентів
students = [
    {"name": "Vlad", "score": 100},
    {"name": "Sviatoslav", "score": 99},
    {"name": "Юстин", "score": 100},
    {"name": "Viktor", "score": 79},
    {"name": "Ярослав", "score": 93}
]
max_score = 100

@app.route('/')
def results():
    return render_template("results.html", students=students, max_score=max_score)

if __name__ == '__main__':
    app.run(debug=True)