const fs = require("fs");
const { request } = require("http");

function logCreater() {
  return (req, res, next) => {
    fs.appendFile(
      "log.txt",
      `\n ${Date.now()} ${req.method}: ${req.path} \n`,
      (err, data) => {
        next();
      }
    );
  };
}

module.exports = {
  logCreater,
};
