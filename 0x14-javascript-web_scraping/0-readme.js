#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];

if (!filePath) { process.exit(1); }

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(data);
});
