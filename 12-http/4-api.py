from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.get_json()  # Отримуємо JSON з POST-запиту



    return jsonify({"message": "Дані отримано", "data": data})

@app.route('/resource', methods=['PUT'])
def update_resource():
    # Логіка для оновлення ресурсу

    return 'Ресурс оновлено', 200

@app.route('/resource', methods=['DELETE'])
def delete_resource():
    # Логіка для видалення ресурсу
    return 'Ресурс видалено', 200


if __name__ == '__main__':
    app.run(debug=True)



{
  "name": "Андрій",
  "age": 25
}
