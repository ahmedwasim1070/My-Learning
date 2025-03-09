const express = require("express");
const router = express.Router();

const {
  handleGetAllUsers,
  handleUserSubmit,
  handleGetUser,
  handleUserDelete,
  handleUserPatch,
} = require("../controllers");

router
  .route("userData/:id")
  .get(handleGetUser)
  .delete(handleUserDelete)
  .patch(handleUserPatch);

router.post("/pushUserData", handleUserSubmit);

router.get("/userData", handleGetAllUsers);

module.exports = router;
