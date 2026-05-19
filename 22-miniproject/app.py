from flask import Flask, render_template, request, session, redirect
import random
import sqlite3
import time

app = Flask(__name__)
app.secret_key = "secret"

SIZE = 5
MINES_COUNT = 5
DATABASE = "game.db"


# ---------------------------------------------------
# СТВОРЕННЯ БАЗИ ДАНИХ
# ---------------------------------------------------
def init_db():
    """
    Створює таблицю результатів якщо її ще немає.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            result TEXT,
            seconds INTEGER
        )
        """
    )

    conn.commit()
    conn.close()


# ---------------------------------------------------
# ЗБЕРЕЖЕННЯ РЕЗУЛЬТАТУ
# ---------------------------------------------------
def save_result(name, result, seconds):
    """
    Зберігає результат гри у базу даних.

    Args:
        name (str): ім'я гравця
        result (str): WIN або LOSE
        seconds (int): час гри у секундах
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO results(name, result, seconds) VALUES ({name}, {result}, {seconds})"
    )

    conn.commit()
    conn.close()


# ---------------------------------------------------
# ОТРИМАННЯ РЕЗУЛЬТАТІВ
# ---------------------------------------------------
def get_results():
    """
    Повертає останні результати гри.
    """

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, result, seconds FROM results ORDER BY id DESC LIMIT 10"
    )

    results = cursor.fetchall()

    conn.close()

    return results


# ---------------------------------------------------
# СТВОРЕННЯ МІН
# ---------------------------------------------------
def create_board():
    """
    Створює список випадкових координат мін.
    """

    mines = []

    while len(mines) < MINES_COUNT:

        coord = (
            random.randint(0, SIZE - 1),
            random.randint(0, SIZE - 1)
        )

        if coord not in mines:
            mines.append(coord)

    return mines


# ---------------------------------------------------
# ПІДРАХУНОК МІН
# ---------------------------------------------------
def count_mines(x, y, mines):
    """
    Рахує кількість мін навколо клітинки.
    """

    count = 0

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:

            if dx == 0 and dy == 0:
                continue

            nx = x + dx
            ny = y + dy

            if (nx, ny) in mines:
                count += 1

    return count


# ---------------------------------------------------
# ПЕРЕВІРКА ПЕРЕМОГИ
# ---------------------------------------------------
def check_win(opened, mines):
    """
    Перевіряє чи відкрив гравець усі клітинки без мін.
    """

    return len(opened) == (SIZE * SIZE) - len(mines)


# ---------------------------------------------------
# СТОРІНКА ВВЕДЕННЯ ІМЕНІ
# ---------------------------------------------------
@app.route("/start", methods=["GET", "POST"])
def start():
    """
    Сторінка введення імені.
    """

    if request.method == "POST":

        name = request.form.get("name")

        session.clear()

        session["name"] = name

        return redirect("/")

    return render_template("start.html")


# ---------------------------------------------------
# ГОЛОВНА СТОРІНКА
# ---------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def main():
    """
    Головна сторінка гри.
    """

    # Якщо ім'я не введено
    if "name" not in session:
        return redirect("/start")

    name = session["name"]

    # Створення нової гри
    if "mines" not in session:

        session["mines"] = create_board()
        session["opened"] = []
        session["game_over"] = False
        session["win"] = False

        # Час початку гри
        session["start_time"] = time.time()

    mines = [tuple(m) for m in session["mines"]]
    opened = [tuple(o) for o in session["opened"]]

    game_over = session["game_over"]
    win = session["win"]

    # Якщо натиснули на клітинку
    if request.method == "POST" and not game_over:

        x = int(request.form.get("x"))
        y = int(request.form.get("y"))

        coord = (x, y)

        if coord not in opened:
            opened.append(coord)

        # Програш
        if coord in mines:

            game_over = True

            seconds = int(time.time() - session["start_time"])

            save_result(name, "LOSE", seconds)

        # Перемога
        elif check_win(opened, mines):

            game_over = True
            win = True

            seconds = int(time.time() - session["start_time"])

            save_result(name, "WIN", seconds)

        session["opened"] = opened
        session["game_over"] = game_over
        session["win"] = win

    # Поточний час гри
    seconds = int(time.time() - session["start_time"])

    # Створюємо поле
    board = []

    for x in range(SIZE):

        row = []

        for y in range(SIZE):

            coord = (x, y)

            cell = {
                "x": x,
                "y": y,
                "opened": coord in opened,
                "mine": coord in mines,
                "count": count_mines(x, y, mines)
            }

            row.append(cell)

        board.append(row)

    results = get_results()

    return render_template(
        "index.html",
        board=board,
        size=SIZE,
        game_over=game_over,
        win=win,
        seconds=seconds,
        name=name,
        results=results
    )


# ---------------------------------------------------
# ПЕРЕЗАПУСК ГРИ
# ---------------------------------------------------
@app.route("/restart")
def restart():
    """
    Перезапускає гру.
    """

    name = session.get("name")

    session.clear()

    session["name"] = name

    return redirect("/")


if __name__ == "__main__":

    init_db()

    app.run(debug=True)