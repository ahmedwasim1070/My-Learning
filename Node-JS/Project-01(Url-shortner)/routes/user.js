const express = require("express");
const { handleUserSignup, handlUserLogin } = require("../controller/user.js");

const router = express.Router();

router.post("/signup", handleUserSignup);
router.post("/login", handlUserLogin);
router.get("/signup", (req, res) => {
  res.render("signup");
});
router.get("/login", (req, res) => {
  res.render("login");
});

module.exports = router;
