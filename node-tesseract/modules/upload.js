const mongoose = require("mongoose");
mongoose.Promise = global.Promise;
// mongoose.connect("mongodb://localhost:27017/majorproject");
// Connection URL
var url = "mongodb://localhost:27017/majorproject";
// Use connect method to connect to the server
mongoose.connect(url, function(err, db) {
  console.log("Connected correctly to server");
});
const nameSchema = new mongoose.Schema({
    imgtxt: String,
    img: String
});
nameSchema.index({ img: 'text', imgtxt: 'text' });
const User = mongoose.model("image", nameSchema);
User.createIndexes();

// console.log(db.getName());
module.exports = User;