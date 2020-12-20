//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const upload =require("express-fileupload");

const app = express();
app.use(upload())
app.set('view engine', 'ejs');

app.listen(3000, function() {
    console.log('server running on port 3000');
} )

app.get("/", function(req, res){
  res.sendFile(__dirname + '/home.html');
});

app.post("/", function(req, res){
  if(req.files){
    console.log(req.files);
    var file = req.files.file;
    var filename = file.name
    file.mv('./uploads/'+filename,function(err){
      if(err){res.send(err)}
    })
    console.log('Running python code');

    // Use child_process.spawn method from
    // child_process module and assign it
    // to variable spawn
    var spawn = require("child_process").spawn;
    // Parameters passed in spawn -
    // 1. type_of_script
    // 2. list containing Path of the script
    //    and arguments for the script

    // E.g : http://localhost:3000/name?firstname=Levente
    var process = spawn('python',['image to text.py',file.name]);

    var output = '';
    process.stdout.on('data', function(data) {

        console.log("Sending Info")
        res.send(data.toString('utf8'));
    });

    console.log(output);
     }




});
