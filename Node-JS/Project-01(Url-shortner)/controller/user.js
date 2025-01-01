const user = require("../models/user.js");
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
  const token = sessionIdToUserMap.setUser(user);
  res.cookie("uid", token);
  return res.redirect("/url/ui");
}

module.exports = { handleUserSignup, handlUserLogin };
