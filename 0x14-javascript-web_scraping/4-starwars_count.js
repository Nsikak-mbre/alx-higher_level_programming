#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const userId = '18';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const films = data.results;
    const userMovies = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${userId}/`)
    );
    console.log(userMovies.length);
  }
});
