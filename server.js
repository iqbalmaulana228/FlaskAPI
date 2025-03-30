const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors()); // Enable CORS for all routes

// Dummy data for countries
const countries = [
    { name: "United States", uniqueness: "Home of Hollywood" },
    { name: "Japan", uniqueness: "Land of the Rising Sun" },
    { name: "Brazil", uniqueness: "Famous for Carnival" },
    { name: "India", uniqueness: "Home of Bollywood" },
    { name: "Australia", uniqueness: "Known for its unique wildlife" },
    { name: "France", uniqueness: "Famous for the Eiffel Tower" },
    { name: "Italy", uniqueness: "Home of Pizza and Pasta" },
    { name: "Canada", uniqueness: "Known for its maple syrup" },
    { name: "Germany", uniqueness: "Famous for its engineering" },
    { name: "South Africa", uniqueness: "Home of the Big Five" }
];

// GET /countries
app.get('/countries', (req, res) => {
    res.json(countries);
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
