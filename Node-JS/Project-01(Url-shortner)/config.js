const mongose = require("mongoose");

async function handleMongoseConnecet(url) {
  return mongose.connect(url);
}

module.exports = {
  handleMongoseConnecet,
};
