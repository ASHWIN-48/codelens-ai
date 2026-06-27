require('dotenv').config();

module.exports = {
    PORT: process.env.PORT || 3000,
    PYTHON_SERVICE_URL: process.env.PYTHON_SERVICE_URL || 'http://localhost:8000'
};