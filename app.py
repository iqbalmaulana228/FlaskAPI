from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dummy data for items
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

# List to store logs
log_entries = []

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
    log_entry = f'Created item: {new_item}'
    log_entries.append(log_entry)
    logger.info(log_entry)
    return jsonify(new_item), 201

# PUT /items/<id>
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item.update(request.json)
        log_entry = f'Updated item: {item}'
        log_entries.append(log_entry)
        logger.info(log_entry)
        return jsonify(item)
    return ('', 404)

# DELETE /items/<id>
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    log_entry = f'Deleted item with ID: {item_id}'
    log_entries.append(log_entry)
    logger.info(log_entry)
    return ('', 204)

# GET /logs
@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(log_entries)

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Running on port 5000
