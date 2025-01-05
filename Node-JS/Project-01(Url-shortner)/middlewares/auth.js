const { sessionIdToUserMap } = require("../service/auth.js");

async function rsetrictToLoggedinUserOnly(req, res, next) {
  // const userUid = req.cookies?.uid;
  console.log(req.headers);
  const userUid = req.headers["authorization"];
  if (!userUid) return res.redirect("/user/login");
  const token = userUid.split("Bearer ")[1];

  const user = sessionIdToUserMap.getUser(token);
  if (!user) return res.redirect("/user/login");
  req.user = user;
  next();
}

module.exports = {
  rsetrictToLoggedinUserOnly,
};
