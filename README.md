# REST API Project

This project contains a REST API implemented in JavaScript using Node.js and Express. The API provides endpoints for managing items and serving random country names.

## Setup Instructions

### Prerequisites
- Ensure that Node.js is installed on your system. If not, download and install it from [nodejs.org](https://nodejs.org/).

### Installation
1. Navigate to the `RestAPI` directory:
   ```bash
   cd RestAPI
   ```

2. Install the required dependencies:
   ```bash
   npm install express cors
   ```

### Running the Server
- To run the item management API:
  ```bash
  node app.js
  ```

- To run the country names API:
  ```bash
  node server.js
  ```

### API Endpoints
- **Item Management API (`app.js`):**
  - `GET /items`: Retrieve all items.
  - `GET /items/:id`: Retrieve a specific item by ID.
  - `POST /items`: Create a new item.
  - `PUT /items/:id`: Update an existing item by ID.
  - `DELETE /items/:id`: Delete an item by ID.

- **Country Names API (`server.js`):**
  - `GET /countries`: Retrieve a list of random country names and their unique characteristics.

### Testing the API
- Use a tool like Postman or your web browser to test the endpoints.
- Access the endpoints at `http://localhost:5000/items` or `http://localhost:5000/countries`.

## Notes
- Ensure that both servers are running on different ports if you are testing them simultaneously.
