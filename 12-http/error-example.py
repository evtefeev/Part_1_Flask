from flask import Flask, abort

app = Flask(__name__)

@app.route('/restricted')
def restricted():
    abort(403)  # Доступ заборонений


@app.errorhandler(404)
def page_not_found(error):
    return "Такої сторінки не існує!", 404


if __name__ == '__main__':
    app.run(debug=True)
