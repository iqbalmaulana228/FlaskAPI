const express = require('express');
const cors = require('cors');
const fs = require('fs');

const app = express();
app.use(cors()); // Enable CORS for all routes
app.use(express.json()); // Middleware to parse JSON bodies

let items = JSON.parse(fs.readFileSync('data.json', 'utf8'));

// GET /items
app.get('/items', (req, res) => {
    // Reload items from data.json to ensure we have the latest data
    items = JSON.parse(fs.readFileSync('data.json', 'utf8'));
    res.json(items);
});

// GET /items/:id
app.get('/items/:id', (req, res) => {
    // Reload items from data.json to ensure we have the latest data
    items = JSON.parse(fs.readFileSync('data.json', 'utf8'));
    const item = items.find(i => i.id === parseInt(req.params.id));
    if (item) {
        res.json(item);
    } else {
        res.status(404).send('Item not found');
    }
});

// POST /items
app.post('/items', (req, res) => {
    const newItem = req.body;
    newItem.id = items.length + 1;
    items.push(newItem);
    
    // Save updated items to data.json
    fs.writeFileSync('data.json', JSON.stringify(items, null, 2));
    
    res.status(201).json(newItem);
});

// PUT /items/:id
app.put('/items/:id', (req, res) => {
    const item = items.find(i => i.id === parseInt(req.params.id));
    if (item) {
        Object.assign(item, req.body);
        
        // Save updated items to data.json
        fs.writeFileSync('data.json', JSON.stringify(items, null, 2));
        
        res.json(item);
    } else {
        res.status(404).send('Item not found');
    }
});

// DELETE /items/:id
app.delete('/items/:id', (req, res) => {
    items = items.filter(i => i.id !== parseInt(req.params.id));
    
    // Save updated items to data.json
    fs.writeFileSync('data.json', JSON.stringify(items, null, 2));
    
    res.status(204).send();
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
