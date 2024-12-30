// Creating http server from scratch using node only

// const http=require("http");
// const fs=require("fs");
// const url =require("url");

// const myServer=http.createServer((req,res)=>{
//     const log=`${Date.now()}: ${req.url} New Req Recieved\n`;
//     const myUrl = url.parse(req.url,true);
//     console.log(myUrl);
//     fs.appendFile('log.txt',log,(err,data)=>{
//         switch(myUrl.pathname){
//             case '/':
//                  res.end("HomePage");
//                  break;
//             case '/about':
//                  const userName=myUrl.query.my_name;
//                  res.end(`Hello ${userName}`);
//                  break;
//             default:
//                 res.end("404 not found ! ");
//         }
//     })
// });

// myServer.listen( 8000 , () => console.log( ' Server Started ! ' ) );

// Express JS (Making of server)

// const express=require("express");
// const app=express();
// const PORT=8000;
// app.listen(PORT,()=> console.log(`Server Started at PORT: ${PORT}`))

// Rest Full API
const express = require("express");
const fs = require("fs");
const userData = require("./user_data.json");
const { type } = require("os");

const { connectMongoDB } = require("./config.js");
const { logCreater } = require("./middlewares");
const userRouter = require("./routes/user");

const app = express();
const PORT = 8000;

// Connection
connectMongoDB("mongodb://localhost:27017")
  .then(() => console.log("DB connected"))
  .catch((err) => console.log("Failed to connect", err));

// Middle ware
app.use(express.urlencoded({ extended: false }));

app.use(logCreater("log.txt"));

// Routes
app.use("/api/user", userRouter);

app.listen(PORT, () => console.log(`Server Started at PORT: ${PORT}`));
