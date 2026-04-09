from flask import Flask, request, jsonify


app = Flask(__name__)


# Список користувачів
users = {
    1: {"name": "Alex", "email": "alex@example.com"},
    2: {"name": "Maria", "email": "maria@example.com"}
}


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()  # Отримуємо JSON-дані з PUT-запиту
        users[user_id]["name"] = data.get("name", users[user_id]["name"])
        users[user_id]["email"] = data.get("email", users[user_id]["email"])
        return jsonify({"message": "User updated!", "user": users[user_id]})
    else:
        return jsonify({"error": "User not found"}), 404



# @app.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     if user_id in users:
#         del users[user_id]
#         return jsonify({"message": f"User {user_id} deleted successfully!"})
#     else:
#         return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)



