from flask import Flask, render_template, request, redirect, url_for

# Імпорт моделей таблиць та сессії для роботи з БД
from databases import Session, Product, Order
from api import get_all_products
from helpers import apply_price

app = Flask(__name__)

external_products = get_all_products()
external_products = apply_price(external_products, 10)


# Головна сторінка
@app.route("/")
def index():
    return render_template("index.html")


# Сторінка з усіма товарами
@app.route("/products")
def products():
    with Session() as session:
        all_products = session.query(Product).all()  # Взяття усіх товарів з БД

    return render_template(
        "products.html", products=all_products
    )  # Передача html-файлу разом з інформацією про товари


@app.route("/fake_products")
def fake_products():
    return render_template(
        "products.html", products=external_products
    )  # Передача html-файлу разом з інформацією про товари


# Сторінка замовлення
@app.route("/order/<int:product_id>", methods=["GET", "POST"])
def order(product_id):
    with Session() as session:
        count = session.query(Product).count()
        if product_id > count:
            for product in external_products:
                if product["id"] == product_id:
                    break
        else:
            product = session.query(Product).get(
                product_id
            )  # Забираємо данні про товар за його id

        if not product:
            return "Товар не знайдено", 404

        if request.method == "POST":
            phone = request.form["phone"]
            email = request.form["email"]

            # Створюємо нове замовлення
            new_order = Order(phone=phone, email=email, product_id=product_id)
            session.add(new_order)
            session.commit()

            return redirect(
                url_for("index")
            )  # Повертаємо користувача на головну сторінку
        return render_template(
            "order.html", product=product
        )  # Передаємо данні про товар разом з html-файлом


if __name__ == "__main__":
    app.run(debug=True, port=8080)
