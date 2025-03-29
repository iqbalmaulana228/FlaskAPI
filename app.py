from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def serve_index():
    return send_from_directory('', 'index.html')

# GET /welcome
@app.route('/welcome', methods=['GET'])
def welcome():
    """Returns a welcome message"""
    return jsonify({'message': 'Welcome to the Flask API!'})

# GET /items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET /items/<id>
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    return jsonify(item) if item else ('', 404)

# POST /items
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# PUT /items/<id>
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item.update(request.json)
        return jsonify(item)
    return ('', 404)

# DELETE /items/<id>
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Running on port 5000
