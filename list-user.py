from flask import Flask, jsonify

app = Flask(__name__)

users = {
    'user1': {},
    'user2': {},
    'user3': {},
}

# Route for listing users
@app.route('/list_users', methods=['GET'])
def list_users():
    user_list = list(users.keys())
    return jsonify({'users': user_list})

if __name__ == '__main__':
    app.run(debug=True)
