from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Дані про студентів
students = [
    {"name": "Vlad", "score": 100},
    {"name": "Sviatoslav", "score": 99},
    {"name": "Юстин", "score": 100},
    {"name": "Viktor", "score": 79},
    {"name": "Ярослав", "score": 93},
]
max_score = 100


@app.route("/", methods=["GET", "PUT", "POST"])
def results():
    method = request.form.get("_method")
    if request.method == "PUT" or method == "PUT":
        name = request.form.get("name")
        score = int(request.form.get("score"))
        print(name, score)
        for student in students:
            if student["name"] == name:
                student["score"] = score
                
    return render_template("results.html", students=students, max_score=max_score)


@app.route("/add-student", methods=["POST", "GET"])
def add_student():
    if request.method == "POST":
        name = request.form.get("name")
        score = request.form.get("score")
        students_add = {}
        students_add["name"] = name
        students_add["score"] = score
        students.append(students_add)
        return redirect(url_for("results"))
   
    return render_template("form.html")


@app.route("/update_score/<name>", methods=["POST", "GET"])
def update_score(name):
    score = 0
    for student in students:
        if student["name"] == name:
            score = student["score"]
    return render_template("update_form.html", name=name, score=score)


if __name__ == "__main__":
    app.run(debug=True)
