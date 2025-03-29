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
- **GET /**: Serves the `index.html` file.
- **GET /welcome**: Returns a welcome message.
- **GET /items**: Retrieves a list of items.
- **GET /items/<id>**: Retrieves a specific item by ID.
- **POST /items**: Creates a new item.
- **PUT /items/<id>**: Updates an existing item by ID.
- **DELETE /items/<id>**: Deletes an item by ID.

## Example Requests
### Get Welcome Message
```bash
curl http://127.0.0.1:5000/welcome
```

### Get All Items
```bash
curl http://127.0.0.1:5000/items
```

## License
This project is licensed under the MIT License.
