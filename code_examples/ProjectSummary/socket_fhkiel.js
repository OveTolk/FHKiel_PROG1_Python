const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });
const cors = require('cors');
const bodyParser = require('body-parser');

app.use(cors());
app.use(bodyParser.json()); // Middleware zum Parsen des JSON-Bodys

let connectedWebSocket = null; // Hier speichern wir die WebSocket-Verbindung

wss.on('connection', (ws) => {
  console.log('WebSocket connection established.');

  // Speichere die WebSocket-Verbindung, wenn eine Verbindung hergestellt wird
  connectedWebSocket = ws;

  ws.on('message', (message) => {
    console.log(`Received message from WebSocket: ${message}`);
  });
});

// Deine HTTP-Route für creategraph
app.get('/creategraph', async (req, res) => {    
  // Daten aus dem HTTP-Request empfangen
  const data = req.body[0];
  console.log(data)
  // Überprüfe, ob eine WebSocket-Verbindung besteht
  if (connectedWebSocket) {
    try {
      // Sende die Daten als JSON an den WebSocket-Client
      connectedWebSocket.send(JSON.stringify(data));
      console.log('Daten an WebSocket-Client gesendet.');
    } catch (error) {
      console.error('Fehler beim Senden der Daten an WebSocket-Client:', error);
    }
  }

  // Senden der HTTP-Antwort
  res.status(200).send('Daten erfolgreich an den Vue.js-Webserver gesendet');
});

server.listen(3007, () => {
  console.log('Server listening on port 3007');
});
