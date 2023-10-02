from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

# Route for user signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required'}), 400

    username = data['username']
    password = data['password']

    if username in users:
        return jsonify({'error': 'Username already exists'}), 400

    # Storing the user in the database
    users[username] = {'password': password}

    return jsonify({'message': 'Signup successful'}), 201

if __name__ == '__main__':
    app.run(debug=True)
