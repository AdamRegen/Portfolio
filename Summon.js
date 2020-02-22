//Summon
//Data codes retrieved from;
//https://github.com/bradtraversy/mongo_file_uploads
//https://github.com/aheckmann/gridfs-stream
//https://github.com/devconcept/multer-gridfs-storage

const port = 8086,
        express = require('express');
        app = express();
        bodyParser = require("body-parser");
        path = require("path");
        crypto = require("crypto");
        mongoose = require("mongoose");
        multer = require("multer");
        GridFsStorage = require("multer-gridfs-storage");
        Grid = require("gridfs-stream");
        methOver = require("method-override");

//Middleware        
app.use(bodyParser.json());
app.use(methOver('_method'));
app.set('view engine', 'ejs');

//Database 
const uri = "mongodb+srv://root:LogAccess123@summoncluster-sz0dk.mongodb.net/test?retryWrites=true&w=majority";
        client = mongoose.createConnection(uri,{useNewUrlParser: true, useUnifiedTopology: true})

//Init gfs //taken from : https://github.com/aheckmann/gridfs-stream
let gfs;

client.once('open', function() {
    gfs = Grid(client.db, mongoose.mongo);
    gfs.collection('uploads')

  })

//Storage Engine //taken from : https://github.com/devconcept/multer-gridfs-storage
const storage = new GridFsStorage({
    url: uri,
    file: (req, file) => {
      return new Promise((resolve, reject) => {
          //encrypts file name
        crypto.randomBytes(16, (err, buf) => {
          if (err) {
            return reject(err);
          }
          const filename = buf.toString('hex') + path.extname(file.originalname);
          const fileInfo = {
            filename: filename,
            bucketName: 'uploads'
          };
          resolve(fileInfo);
        });
      });
    }
  });
  const upload = multer({ storage });

//Loads form
app.get('/',(req, res) => {
    gfs.files.find().toArray((err, files) => {
        if (!files || files.length === 0){
            res.render('Summon', {files: false});
            }else {
                files.map(file => {
                    if (file.contentType === 'image/jpeg' || file.contentType === 'image/png')
                    {
                        file.isImage = true;
                    }else {
                        file.isImage = false;
                    }
                });
                res.render('Summon', {files: files});
            }      
    });
});

//Upload file to Database
app.post('/fileupload', upload.single('filetoupload'), (req, res) => {
    res.redirect('/');
});

//Display all files in json
app.get('/files',(req,res) => {
    gfs.files.find().toArray((err, files) => {
        if (!files || files.length === 0){
            return res.status(404).json({
                err: 'No files exist'
            });
            
        }

        return res.json(files);
    });
});

//Display file in json
app.get('/files/:filename',(req,res) => {
    gfs.files.findOne({filename: req.params.filename}, (err, file) => {
        if (!file || file.length === 0){
            return res.status(404).json({
                err: 'No files exist'
            });
            
        }

        return res.json(file);
    });
});

//Display image in json
app.get('/image/:filename', (req, res) => {
    gfs.files.findOne({ filename: req.params.filename }, (err, file) => {
      // Check if file
      if (!file || file.length === 0) {
        return res.status(404).json({
          err: 'No file exists'
        });
      }
  
      // Check if image
      if (file.contentType === 'image/jpeg' || file.contentType === 'image/png') {
        // Read output to browser
        const readstream = gfs.createReadStream(file.filename);
        readstream.pipe(res);
      } else {
        res.status(404).json({
          err: 'Not an image'
        });
      }
    });
  });

//Delete file
app.delete('/files/:id', (req, res) => {
    gfs.remove({ _id: req.params.id, root: 'uploads' }, (err, gridStore) => {
      if (err) {
        return res.status(404).json({ err: err });
      }
  
      res.redirect('/');
    });
  });

// Downloading a single file
app.get('/file/:filename', (req, res) => {
  gfs.exist({ _id: id }, function(err, found) {
    if (err) {
      handleError(err); 
      return;
    }

    if (!found) {
      res.send('Error on the database looking for the file.')
      return;
    }

    // We only get here if the file actually exists, so pipe it to the response
    gfs.createReadStream({ _id: id }).pipe(res);
  });
});
//Listens to  port
app.listen(port, function(error) {
    if (error) {
        console.log("Something went wrong", error)
    }else {
        console.log("Server Activated - Listening to port" + port)
    }
})