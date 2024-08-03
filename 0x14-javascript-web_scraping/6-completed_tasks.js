#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const userTaskDone = {};
    todos.forEach(todo => {
      if (todo.completed) {
        if (userTaskDone[todo.userId]) {
          userTaskDone[todo.userId]++;
        } else {
          userTaskDone[todo.userId] = 1;
        }
      }
    });
    console.log(JSON.stringify(userTaskDone, null, 2));
  }
});
