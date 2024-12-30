const user = require("../models/user.js");
const url = require("../models/model.js");
const { v4: uuidv4 } = require("uuid");
const { sessionIdToUserMap } = require("../service/auth.js");

async function handleUserSignup(req, res) {
  const { name, email, password } = req.body;
  await user.create({ name, email, password });
  return res.redirect("/url/ui");
}

async function handlUserLogin(req, res) {
  const { email, password } = req.body;
  const userData = await user.findOne({ email, password });
  if (!userData)
    return res.render("login", {
      error: "The email or password was incorrect !",
    });
  const sessionId = uuidv4();
  sessionIdToUserMap.setUser(sessionId, userData);
  res.cookie("uid", sessionId);
  return res.redirect("/url/ui");
}

module.exports = { handleUserSignup, handlUserLogin };
