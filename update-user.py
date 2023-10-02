from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    'user1': {'name': 'devyansh somvanshi', 'email': 'devyansh@example.com'},
    'user2': {'name': 'deepander sehrawat', 'email': 'deepander@example.com'},
    'user3': {'name': 'saksham nehra', 'email': 'saksham@example.com'},
}

# Route for updating a user
@app.route('/update_user/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({'error': f'User {username} not found'}), 404

    data = request.get_json()

    if 'name' in data:
        users[username]['name'] = data['name']

    if 'email' in data:
        users[username]['email'] = data['email']

    return jsonify({'message': f'User {username} updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
