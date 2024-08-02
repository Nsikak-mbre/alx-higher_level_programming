#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const writeTo = process.argv[3];

fs.writeFile(filePath, writeTo, (err) => {
  if (err) {
    console.error(err);
  }
});
