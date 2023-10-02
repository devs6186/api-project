from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data (replace with a real database)
users = {
    "user1": {
        "password": "password1",
        "email": "user1@example.com"
    },
    "user2": {
        "password": "password2",
        "email": "user2@example.com"
    }
}

# Route for user login
@app.route('/', methods=['GET'])
def home():
    return users

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # print(not data)
    # print("username" not in data)
    # print("password" not in data)
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid request"}), 400

    username = data["username"]
    password = data["password"]

    print(username)
    print(password)

    if username in users and users[username]["password"] == password:
        return jsonify({"message": "Login successful", "email": users[username]["email"]})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
