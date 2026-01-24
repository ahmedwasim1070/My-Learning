// Sockets helps to read data in realtime
// HTTP
import http from "http";
// Express
import express from "express";
// Path resolver
import path from "path";
// Socket IO
import { Server } from "socket.io";

// Creates an express app
const app = express();
// Creates http server with express app
const server = http.createServer(app);

// IO for socket.io
const io = new Server(server);

// IO on connection
io.on("connection", (socket) => {
  socket.on("user-message", (message) => {
    io.emit("message", message);
  });
});

// Resolves path of file
app.use(express.static(path.resolve("./public")));

// Get request for that route
app.get("/", (req, res) => {
  return res.sendFile(path.resolve("./public/index.html"));
});

// PORT
const PORT = 8000;

// Starts server at that port (use `server.listen`, not `app.listen`)
server.listen(PORT, () => console.log(`Server started at port ${PORT}`));
