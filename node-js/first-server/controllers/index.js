const database = require("../models/user.js");

async function handleGetAllUsers(req, res) {
  const allUser = await database.find({});
  const html = `
      <ul>
        ${allUser.map((user) => `<li>${user.firstName}</li>`).join("")}
      </ul>
      `;
  res.send(html);
}

async function handleUserSubmit(req, res) {
  const body = req.body;
  if (!body || !body.first_name || !body.email) {
    return res.status(400).json({ message: "All fields are required..." });
  }

  try {
    const result = await database.create({
      firstName: body.first_name,
      lastName: body.lastName,
      email: body.email,
      gender: body.gender,
      jobTitle: body.job_title,
    });

    return res.status(201).json({ msg: "success" });
  } catch {
    console.error("Error creating user:", error);
    res.status(500).json({ message: "Internal Server Error" });
  }
}

async function handleGetUser(req, res) {
  const userResult = await database.findById(req.params.id);
  return res.json(userResult);
}

async function handleUserDelete(req, res) {
  const id = Number(req.params.id);
  const userIdx = userData.findIndex((user) => user.id === id);
  if (userIdx === -1) {
    return res.status(404).json({ error: "User Not Found!" });
  }
  userData.splice(userIdx, 1);
  fs.writeFile("./user_data.json", JSON.stringify(userData), (err) => {
    if (err) {
      return res.status(500).json({ error: "Failed to Save deleted data" });
    }
    return res.json({
      status: "success",
      message: `User with ID ${id} deleted ${userIdx}`,
    });
  });
}

async function handleUserPatch(req, res) {
  await database.findByIdAndUpdate(req.params.id, { lastName: "Changed" });
  return res.json({ status: "Sucess" });
}

module.exports = {
  handleGetAllUsers,
  handleUserSubmit,
  handleGetUser,
  handleUserDelete,
  handleUserPatch,
};
