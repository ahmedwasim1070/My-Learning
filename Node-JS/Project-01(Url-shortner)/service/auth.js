class sessionToMap {
  constructor() {
    this.map = new Map();
  }
  setUser(id, user) {
    this.map.set(id, user);
  }
  getUser(id) {
    return this.map.get(id);
  }
}

const sessionIdToUserMap = new sessionToMap();

module.exports = {
  sessionIdToUserMap,
};
