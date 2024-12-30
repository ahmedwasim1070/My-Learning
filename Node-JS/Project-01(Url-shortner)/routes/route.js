const express = require("express");
const {
  handleUrlGenerator,
  hanldeShortUrlReq,
  handleUI,
} = require("../controller/controller.js");

const router = express.Router();

router.get("/redirect/:link", hanldeShortUrlReq);
router.post("/createUrl", handleUrlGenerator);
router.get("/ui", handleUI);

module.exports = router;
