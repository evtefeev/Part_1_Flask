from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Nikita!"


@app.route("/career/")
def career():
    return "Career Page"


@app.route("/feedback/")
def feedback():
    return "Feedback Page"


@app.route('/user/<id>/')
def user_profile(id):
    return "Profile page of user #{}".format(id)


@app.route("/user/<int:id>/")
def user_profile_int(id):
    return f"User ID is: {id+1}"


if __name__ == "__main__":
    app.run()
