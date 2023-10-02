from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400

    username = data['username']

    if username in users:
        return jsonify({'error': 'Username already exists'}), 400

    # Storing the user in the database
    users[username] = {}

    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
