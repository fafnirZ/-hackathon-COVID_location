const express = require("express");
const app = express();
const axios = require("axios");
const bodyParser = require("body-parser");
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;



app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended:true}));

app.get("/", (req, res) => {
    res.render("index");
});

app.get("/join", (req, res) => {
    res.render("join");
});

app.post("/join", (req, res) => {
    let number = req.body.number;
    let postcode = req.body.postcode;
    console.log(number);
    console.log(postcode);
    let object = {
        number:number,
        postcode:postcode
    }
    let payload = JSON.stringify(object)
    const xmlhttp = new XMLHttpRequest();

    xmlhttp.open("POST", "http://localhost:8080/join");
    xmlhttp.setRequestHeader("Content-Type","application/json");
    xmlhttp.send(payload);
    res.redirect("/");
});

app.get("/info", (req, res) => {
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let result = JSON.parse(this.responseText)
            res.render("info", {result:result});
        }
     };
    xmlhttp.open("GET", "http://localhost:8080/info");
    xmlhttp.send();

});


app.get("/about", (req, res) => {
    res.render("about");
});



app.listen(4004, function() {
    console.log("server has started");
  });
  


// setInterval(() => post(), 86400000);

// function post() {
//     const xmlhttp = new XMLHttpRequest();
//     xmlhttp.open("POST", "http://localhost:8080/update");
//     xmlhttp.setRequestHeader("Content-Type","application/json");
//     xmlhttp.send();
// }