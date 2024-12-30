const url = require("../models/model.js");

const char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_";

class stringMaker {
  randomNum(max, min) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  randomString(num) {
    let prev = "";
    for (let i = 0; i < num; i++) {
      const randomNum = this.randomNum(char.length - 1, 0);
      prev = prev + char[randomNum];
    }
    return prev;
  }
}

const generateShortId = new stringMaker();

async function handleUrlGenerator(req, res) {
  const body = req.body;
  if (!body.url) return res.status(400).json({ error: "Url is required ! " });
  const shortID = generateShortId.randomString(8);
  await url.create({
    shortID: shortID,
    redirectUrl: body.url,
    totalClicks: [],
    createdBy: req.user._id,
  });
  return res.render("index", { id: shortID, urls: await url.find({}) });
}

async function hanldeShortUrlReq(req, res) {
  const shortID = req.params.link;
  const chkEntry = await url.findOneAndUpdate(
    {
      shortID,
    },
    {
      $push: {
        totalClicks: {
          timestamps: Date.now(),
        },
      },
    }
  );
  if (!chkEntry)
    return res.status(400).json({ error: "There is no such URL!" });
  res.redirect(chkEntry.redirectUrl);
}

async function handleUI(req, res) {
  const allUrls = await url.find({ createdBy: req.user._id });
  return res.render("index", {
    urls: allUrls,
  });
}

module.exports = {
  handleUrlGenerator,
  hanldeShortUrlReq,
  handleUI,
};
