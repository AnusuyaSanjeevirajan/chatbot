const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Forward chat messages to Flask backend
app.post('/chat', async (req, res) => {
  try {
    const flaskRes = await axios.post('http://localhost:5000/chat', req.body);
    res.json(flaskRes.data);
  } catch (error) {
    res.status(500).json({ error: 'Error communicating with chatbot backend.' });
  }
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Node.js bridge server running on port ${PORT}`);
}); 