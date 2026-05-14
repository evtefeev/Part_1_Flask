from flask import Flask
from flask import render_template, request
import os

import magic

app = Flask(__name__)

APP_PATH = os.path.dirname(os.path.realpath(__file__))

FILES_PATH = APP_PATH + "/static/users_files"


@app.route("/", methods=["GET", "POST"])
def f_page_1():
    if request.method == "GET":
        return render_template("form.html")

    user_file = request.files.get("user_file")
    file_desc = request.form.get("file_desc")

    if not user_file or not file_desc:
        return render_template("form.html", message="Недостатньо даних")

    # pip install python-magic-bin
    mime = magic.Magic(mime=True)
    file_type = mime.from_buffer(user_file.read(1024))
    user_file.seek(0)

    if file_type not in ["image/png", "image/jpeg", "image/jpg"]:
        return render_template("form.html", message="Обрано файл неправильного типу")

    if user_file.content_length > 1 * 1024 * 1024:
        return render_template("form.html", message="Обрано файл великого розміру, допустимий розмір: менше 10 Мб")

    from werkzeug.utils import secure_filename

    filename = secure_filename(user_file.filename)
    if not filename:
        return render_template("form.html", "Обрано файл неприйнятної назви")

    import uuid
    unique_filename = f"{uuid.uuid4()}_{filename}"

    file_path = os.path.join(FILES_PATH, unique_filename)
    user_file.save(file_path)

    return render_template("form.html", message="Файл успішно заванетажено!")


@app.route("/all_files")
def f_page_2():
    all_data = os.listdir(FILES_PATH)
    return render_template("all_files.html", data=all_data)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
