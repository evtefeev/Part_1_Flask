

from flask import Flask, abort, session
from flask_login import login_required


app = Flask(__name__)


# MAX_CONTENT_LENGTH визначає, скільки максимально даних сервер може прийняти у запит
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# MAX_FORM_MEMORY_SIZE контролює максимальний розмір даних для нефайлових полів форми
app.config['MAX_FORM_MEMORY_SIZE'] = 1024 * 1024  # 1MB

# MAX_FORM_PARTS визначає, скільки максимум полів може бути у формі.
app.config['MAX_FORM_PARTS'] = 50  # Ліміт 50 полів



# Використовувати перевірку автентифікації та ролей у Flask-Login:
@app.route("/admin")
@login_required
def admin_panel():
    current_user = session['current_user']
    if not current_user or current_user.role != "admin":
        abort(403)

    return "Ласкаво просимо до адмін-панелі!"