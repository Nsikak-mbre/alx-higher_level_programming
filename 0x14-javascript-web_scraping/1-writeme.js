#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const filePath = process.argv[2];
const writeTo = process.argv[3];

if (!filePath || !writeTo) { process.exit(1); }

fs.writeFile(filePath, writeTo || '', 'utf-8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
