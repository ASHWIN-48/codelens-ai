const express = require('express');
const cors = require('cors');
const ingestRouter = require('./routes/ingest');
const askRouter = require('./routes/ask');
const docsRouter = require('./routes/docs');
const { PORT } = require('./config');

const app = express();

app.use(cors());
app.use(express.json());

app.use('/api/ingest', ingestRouter);
app.use('/api/ask', askRouter);
app.use('/api/docs', docsRouter);

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', service: 'codelens-node' });
});

app.listen(PORT, () => {
    console.log(`CodeLens Node service running on port ${PORT}`);
});