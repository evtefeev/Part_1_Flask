from flask import Flask
from flask import render_template, request

import os

app = Flask(__name__)

APP_PATH = os.path.dirname(os.path.realpath(__file__))

FILES_PATH = APP_PATH + "/static/users_files"


@app.route("/", methods=["GET", "POST"])
def f_page_1():
    if request.method == "GET":
        return render_template("form.html")

    user_file = request.files.get("user_file")
    file_desc = request.form.get("file_desc")

    file_path = os.path.join(FILES_PATH, user_file.filename)
    user_file.save(file_path)

    return render_template("form.html", message="Файл успішно заванетажено!")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
