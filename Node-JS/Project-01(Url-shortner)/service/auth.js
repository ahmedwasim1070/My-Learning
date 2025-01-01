class sessionToMap {
  constructor() {
    this.jwt = require("jsonwebtoken");
    this.key = "!@#$%";
  }
  setUser(user) {
    return this.jwt.sign(
      {
        _id: user.id,
        email: user.email,
      },
      this.key
    );
  }
  getUser(token) {
    if (!token) return null;
    return this.jwt.verify(token, this.key);
  }
}

const sessionIdToUserMap = new sessionToMap();

module.exports = {
  sessionIdToUserMap,
};
