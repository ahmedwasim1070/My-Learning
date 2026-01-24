// NODE Streams helps to read large files without taking too much memory
// Express
import express from "express";
// fs
import fs from "fs";
// Zlib
import zlib from "zlib";

// Creates an app
const app = express();

// Zipping file while reading it
fs.createReadStream("./public/100mb-examplefile-com.txt").pipe(
  zlib.createGzip().pipe(fs.createWriteStream("./public/sampele.zip"))
);

// Get request for default page
app.get("/", (req, res) => {
  // Creatse a text stera
  const stream = fs.createReadStream(
    "./public/100mb-examplefile-com.txt",
    "utf-8"
  );
  //   Starts writing the text file
  stream.on("data", (chunk) => res.write(chunk));
  //   Ends writing the text file
  stream.on("end", () => res.end());
});

// Starts the server
app.listen(8080, () => console.log("Server started at http://localhost:8080"));
