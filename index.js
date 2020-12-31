const express = require('express')
const {spawn} = require('child_process');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
const port = 3000
app.post('/calculate_carbon_usage', (req, res) => {
 console.log(req.body)
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
 res.send(dataToSend)
 });
 
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))