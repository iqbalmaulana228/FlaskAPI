# Flask API Documentation

## Project Overview
This project is a simple Flask API that serves as a backend for a web application. It includes endpoints for retrieving, creating, updating, and deleting items, as well as a welcome message endpoint.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd RestAPI
   ```
3. Install the required packages:
   ```bash
   pip install flask flask-cors
   ```

## Usage Instructions
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. The application will be running on `http://127.0.0.1:5000`.

## API Endpoints

### 1. **GET /** 
- **Description**: Serves the `index.html` file.
- **Response**: HTML content of the index page.

### 2. **GET /welcome**
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  {
      "message": "Welcome to the Flask API!"
  }
  ```

### 3. **GET /items**
- **Description**: Retrieves a list of items.
- **Response**:
  ```json
  [
      {"id": 1, "name": "Item 1"},
      {"id": 2, "name": "Item 2"},
      {"id": 3, "name": "Item 3"}
  ]
  ```

### 4. **GET /items/<id>**
- **Description**: Retrieves a specific item by ID.
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Item 1"
  }
  ```
- **Error Response**: Returns 404 if the item is not found.

### 5. **POST /items**
- **Description**: Creates a new item.
- **Request Body**:
  ```json
  {
      "name": "New Item"
  }
  ```
- **Response**:
  ```json
  {
      "id": 4,
      "name": "New Item"
  }
  ```

### 6. **PUT /items/<id>**
- **Description**: Updates an existing item by ID.
- **Request Body**:
  ```json
  {
      "name": "Updated Item"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "name": "Updated Item"
  }
  ```

### 7. **DELETE /items/<id>**
- **Description**: Deletes an item by ID.
- **Response**: Returns 204 No Content on success.

## Example Requests
### Get Welcome Message
```bash
curl http://127.0.0.1:5000/welcome
```

### Get All Items
```bash
curl http://127.0.0.1:5000/items
```

### Create a New Item
```bash
curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name": "New Item"}'
```

### Update an Existing Item
```bash
curl -X PUT http://127.0.0.1:5000/items/1 -H "Content-Type: application/json" -d '{"name": "Updated Item"}'
```

### Delete an Item
```bash
curl -X DELETE http://127.0.0.1:5000/items/1
```

## Notes
- Ensure that CORS is enabled in your Flask application to allow requests from different origins.
- The application is designed to run on `http://127.0.0.1:5000`.

## License
This project is licensed under the MIT License.
