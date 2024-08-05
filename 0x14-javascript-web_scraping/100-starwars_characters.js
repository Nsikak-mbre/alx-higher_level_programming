#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, response, body) => {
  if (err) { console.error(err); }
  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach((charUrl) => {
      request(charUrl, (err, response, body) => {
        if (!err && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
