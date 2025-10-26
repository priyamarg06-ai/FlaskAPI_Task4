from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {
    1: {"name": "Priya", "email": "priya@example.com"},
    2: {"name": "Rahul", "email": "rahul@example.com"}
}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data['name'], "email": data['email']}
    return jsonify({"message": "User added successfully", "user": users[new_id]}), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id in users:
        users[user_id].update(data)
        return jsonify({"message": "User updated", "user": users[user_id]})
    return jsonify({"error": "User not found"}), 404

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted_user})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
