#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const writeTo = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    fs.writeFile(writeTo, body, (err) => {
      if (err) {
        console.error('err');
      }
    });
  }
});
