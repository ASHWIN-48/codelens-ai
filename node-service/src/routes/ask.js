const express = require('express');
const axios = require('axios');
const { PYTHON_SERVICE_URL } = require('../config');

const router = express.Router();

router.post('/', async (req, res) => {
    try {
        const response = await axios.post(`${PYTHON_SERVICE_URL}/ask`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).json({
            error: error.response?.data || 'Ask failed'
        });
    }
});

module.exports = router;