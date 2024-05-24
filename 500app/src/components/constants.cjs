require('dotenv').config();

const apiKey = process.env.REACT_APP_API_KEY;
const engineId = process.env.REACT_APP_ENGINE_ID;

module.exports = {
    apiKey,
    engineId
}