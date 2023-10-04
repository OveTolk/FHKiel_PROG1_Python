const express = require('express')
const app = express()
const port = 3004
var cors = require('cors')
var request = require('request')

const corsConfig = {
    credentials: true,
    origin: true,
  };
app.use(cors(corsConfig))

var mysql = require('mysql');

var con = mysql.createConnection({
    host: "85.214.44.144",
    user: "nfc",
    password: "OveNFC2023!",
    database: "nfctags"
});
con.connect(function(err) {
    if (err) throw err;
});
app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.header(
      "Access-Control-Allow-Headers",
      "Origin, X-Requested-With, Content-Type, Accept"
    );
    next();
  });

app.get('/nfcgps', (req, res) => {    
  console.log("params",req.params);
  console.log("query",req.query);
  if(!req.query.date) return res.status(500).send("Table error");
  if(!req.query.time) return res.status(500).send("Item error");
  if(!req.query.lat) return res.status(500).send("quantity error");
  if(!req.query.lng) return res.status(500).send("bestellzeit error");
  if(!req.query.device) return res.status(500).send("bestellzeit error");
  if(!req.query.serialnr) return res.status(500).send("bestellzeit error");
  con.query((`INSERT INTO nfcgps (date, time, lat, lng, device, serial) VALUES ('${req.query.date}', '${req.query.time}', '${req.query.lat}', '${req.query.lng}', '${req.query.device}', '${req.query.serialnr}');`), function (err, result, fields) {
      if (err) throw err;
      console.log(result);
  });
  res.send(true);
})
app.get('/selectall', (req, res) => {    
  con.query("SELECT * FROM nfcgps", function (err, result, fields) {
      if (err) throw err;
      res.json(result);
  });

})
app.get('/items', (req, res) => {    
  console.log("params",req.params);
  console.log("query",req.query);
  if(!req.query.family) return res.status(500).send("Table error");
  if(!req.query.listings) return res.status(500).send("Item error");
  if(!req.query.price) return res.status(500).send("quantity error");
  if(!req.query.time) return res.status(500).send("bestellzeit error");
  con.query((`INSERT INTO csgo (family, listings, price, time) VALUES ('${req.query.family}', '${req.query.listings}', '${req.query.price}', '${req.query.time}');`), function (err, result, fields) {
      if (err) throw err;
      console.log(result);
  });
  res.send(true);
})
app.get('/selectallcs', (req, res) => {    
  con.query("SELECT * FROM csgo;", function (err, result, fields) {
      if (err) throw err;
      res.json(result);
  });

})
app.get('/insertteams', (req, res) => {    
  console.log("params",req.params);
  console.log("query",req.query);
  const date = new Date();
  const updatetime = date.toLocaleString()
  if(!req.query.name) return res.status(500).send("1 error");
  if(!req.query.idtable) return res.status(500).send("2 error");
  if(!req.query.updateby) return res.status(500).send("3 error");
  if(!req.query.linktoinfo) return res.status(500).send("5 error");
  if(!req.query.idspielplan) return res.status(500).send("6 error");
  con.query((`INSERT INTO swrd (name, idtable, updateby, updatetime, linktoinfo, idspielplan) VALUES ('${req.query.name}', '${req.query.idtable}', '${req.query.updateby}', '${updatetime}', '${req.query.linktoinfo}', '${req.query.idspielplan}');`), function (err, result, fields) {
      if (err) throw err;
      console.log(result);
  });
  res.send(true);
})
app.get('/getteams', (req, res) => {    
  con.query("SELECT * FROM swrd;", function (err, result, fields) {
      if (err) throw err;
      res.json(result);
  });

})
app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})  
