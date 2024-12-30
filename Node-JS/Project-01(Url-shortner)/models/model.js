const mongose = require("mongoose");

const urlSchema = new mongose.Schema(
  {
    shortID: {
      type: String,
      required: true,
      unique: true,
    },
    redirectUrl: {
      type: String,
      required: true,
    },
    totalClicks: [
      {
        w: {
          type: Number,
        },
      },
    ],
    createdBy: {
      type: mongose.Schema.Types.ObjectId,
      ref: "user",
    },
  },
  { timestamps: true }
);

const url = mongose.model("url", urlSchema);

module.exports = url;
