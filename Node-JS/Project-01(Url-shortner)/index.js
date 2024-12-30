const express = require("express");
const bodyParser = require("body-parser");
const cookieParser = require("cookie-parser");
const path = require("path");
const { handleMongoseConnecet } = require("./config.js");
const { rsetrictToLoggedinUserOnly } = require("./middlewares/auth.js");

const urlRouter = require("./routes/route.js");
const userRouter = require("./routes/user.js");

const app = express();
const PORT = 8000;

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

app.set("views", path.resolve("./views"));
app.set("view engine", "ejs");

app.use("/url", rsetrictToLoggedinUserOnly, urlRouter);
app.use("/user", userRouter);

handleMongoseConnecet("mongodb://127.0.0.1:27017/urlShortner")
  .then(() => console.log("MongoDB Connected Sucessfully! "))
  .catch((error) => console.log("Failed", error));
app.listen(PORT, () => console.log("server started at port:", 8000));
