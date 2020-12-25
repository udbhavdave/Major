const express = require('express');
const app = express();
const fs = require('fs');
const multer = require('multer');
const reload = require('reload');
const path = require('path')
const { createWorker } = require('tesseract.js');
app.use(express.static('public'))
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
var imgData = require('./modules/upload');
const livereload = require("livereload");
const connectLivereload = require("connect-livereload");
const liveReloadServer = livereload.createServer();
liveReloadServer.watch(path.join(__dirname, '/'));

var uploadData = imgData.find({});
var msg="";
const worker = createWorker({
    logger: m => console.log(m)
});
app.use(connectLivereload());

// Setup storage options to upload file inside upload directoty
const storage = multer.diskStorage({    
    destination: (req, file, cd) => {
        cd(null, './public/uploads')
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname)
    }
});

// Intailized upload with storage options
const upload = multer({ storage }).single('avatar');

app.set("view engine", "ejs");
app.get('/', (req, res) => res.render('index',{ title:'Images', records:msg, success:''}))

app.get('/display',(req, res) => {
    uploadData.exec((err, data) =>{
        if(err) throw err;
        res.render('display',{ title:'Images', records:data, success:''})
    })
})

const displayData = multer();
app.post('/display',displayData.none(), (req, res) =>{
    searchData=req.body.search;
    // const query = { $text: { $search: /$searchData/ } };
    console.log(searchData);
    var uploadData = imgData.find({imgtxt:{$regex: ".*" + searchData + ".*", '$options' : 'i'}});
    
    uploadData.exec((err, data) =>{
        if(err) throw err;
        console.log(data);
        res.render('display',{ title:'Images', records:data, success:''})
    })
    // res.sendStatus(200);
})

// Defined API for handle all requests comes on /upload route (or from index's submit btn click)
app.post('/', (req, res) => {

    // Stored file into upload directory
    upload(req, res, err => {

        // Reading uploaded file from upload directory
        fs.readFile(`./public/uploads/${req.file.originalname}`, (err, data) => {

            // Displaying error if anything goes wrong 
            if(err) return console.error("this is error", err);

             // Self execution function to use async await 
             
              (async () => {
                // Tesseract worker loaded with langague option
                await worker.load();
                await worker.loadLanguage('eng');
                await worker.initialize('eng');

                // Document extraction by recognize method of Tesseract and console result
                const { data: { text } } = await worker.recognize(data);
                console.log(text);

                // insert data into MongoDB

                var mydata = new imgData();
                mydata.imgtxt = text;
                mydata.img = req.file.originalname;
                mydata.save()
                .then(item => {
                    msg="File Uploaded Successfully!";
                    // res.send("File Uploaded Successfully!");
                    res.render('index',{ title:'Images', records:[msg,1], success:''});
                })
                .catch(err => {
                    res.status(400).send("Unable to save to database");
                });
                // Respond send to view with result text and terminated worker after porcess complete
                // res.send(text)
                // await worker.terminate();
              })().catch(error => { console.log('caught', error.message); });
        })
    })
})

const PORT = 5000;
app.listen(PORT, () => console.log("App is running on", PORT));
