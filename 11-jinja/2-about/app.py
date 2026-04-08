from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    username = "Олександр"
    age = 15
    hobbies = ["Програмування", "Музика", "Спорт"]
   

    return render_template('base.html',
                         name=username,# передаємо змінні у шаблон
                         age=age,
                         hobbies=hobbies)



if __name__ == '__main__':
  app.run(debug=True)