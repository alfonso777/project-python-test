from flask import Flask, jsonify

app = Flask(__name__)


USERS = [
        {"id": 1, "username": "Michael Jackson", "nickname": "michaelj", "age": 29},
        {"id": 2, "username": "Fredy Mercury", "nickname": "fmercury", "age": 34},
        {"id": 3, "username": "George Harrison", "nickname": "gharrison", "age": 67}
    ]
def retrieve_users():
    return USERS

def find_user_by(field_name: str, value):
    if not value:
        print(f"Not value received to find user by field {field_name}")
        return None
    retrieved_users = [user for user in USERS if user.get(field_name) == value]
    return retrieved_users


@app.route('/users')
def get_users():
    users = retrieve_users()
    if not users:
        print(f"No user were found")
        return jsonify({'message': 'No users found'}), 404
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'],)
def get_user(user_id):
    if not user_id:
        return jsonify({'message': 'No users id recevied'}), 400
    user = find_user_by("id", user_id)
    if not user:
        print(f"The user {id}={user_id} wasn't found")
        return jsonify({'message': f"User {id}={user_id} wasn't found"}), 404
    return jsonify(user), 200


if __name__ == '__main__':
    app.run(debug=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
