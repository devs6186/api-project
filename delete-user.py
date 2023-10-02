from flask import Flask, request, jsonify

app = Flask(__name__)
users = {
    'user1': {},
    'user2': {},
    'user3': {},
}

# Route for deleting a user
@app.route('/delete_user/<username>', methods=['DELETE'])
def delete_user(username):
    if username in users:
        del users[username]
        return jsonify({'message': f'User {username} deleted successfully'}), 200
    else:
        return jsonify({'error': f'User {username} not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
