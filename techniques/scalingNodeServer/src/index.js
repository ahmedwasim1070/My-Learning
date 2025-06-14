// Divide load of a server on different threads or cores
// node cluster
import cluster from "node:cluster";
// node OS
import os from "os";
// Express
import express from "express";

// CPUS
const totalCpus = os.cpus().length;

if (cluster.isPrimary) {
  for (let i = 0; i < totalCpus; i++) {
    cluster.fork();
  }
} else {
  // Creates app
  const app = express();

  // Get request
  app.get("/", (req, res) => {
    return res.json({
      message: `Hello world ${process.pid}`,
    });
  });

  // Starts the server
  app.listen(8080, () =>
    console.log("Server started at http://localhost:8080")
  );
}
