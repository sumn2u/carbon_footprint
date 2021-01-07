const express = require('express')
const {spawn} = require('child_process');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(function(req, res, next) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type, Authorization');
  next();
});
const port = 3000
app.post('/calculate_carbon_usage', (req, res) => {
 
 const { email, answers, footprint,  footprintbytype,  footprint_delta, footprintbytype_delta, labels_footprint, labels_footprintbytype } = req.body;
 console.log(email, answers, footprint,  footprintbytype,  footprint_delta, footprintbytype_delta, labels_footprint, labels_footprintbytype)
 let dataToSend;
 // spawn new child process to call the python script
 const python = spawn('python3', ['carbon_footprint.py', email, answers]);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });
 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
  // res.send({})
  setTimeout(function(){
    res.download(`${__dirname}/tempdir/footprint_report.pdf`)
  },100)
 
 });
 
})

app.post('/certificate', (req, res) => {
 
 const { firstName, lastName, carbon } = req.body;
 
 let dataToSend;
 // spawn new child process to call the python script
 const python = spawn('python3', ['carbon_certificate.py', firstName, lastName, carbon]);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });
 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
  // res.send({})
 res.download(`${__dirname}/certificate.pdf`)
 });
 
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))