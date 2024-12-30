const { sessionIdToUserMap } = require("../service/auth.js");

async function rsetrictToLoggedinUserOnly(req, res, next) {
  const userUid = req.cookies?.uid;
  if (!userUid) return res.redirect("/user/login");
  const user = sessionIdToUserMap.getUser(userUid);
  if (!user) return res.redirect("/user/login");
  req.user = user;
  next();
}

module.exports = {
  rsetrictToLoggedinUserOnly,
};
