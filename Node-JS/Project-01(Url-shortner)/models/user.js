const mongose = require("mongoose");

const userScehma = new mongose.Schema(
  {
    name: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
  },
  { timestamps: true }
);

const user = mongose.model("user", userScehma);

module.exports = user;
