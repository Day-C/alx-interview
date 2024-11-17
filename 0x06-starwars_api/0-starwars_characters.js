#!/usr/bin/node

const request = require('request');

// get the movie number from collamd line
const season = process.argv[2];

// get the actors details
const url = 'https://swapi-api.alx-tools.com/api/films/' + season;
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    // convert request body into  json format
    const data = JSON.parse(body);
    // console.log(data.title)
    const actors = data.characters;

    for (let i = 0; i < actors.length; i++) {
      // console.log(actors[i])
      // make a request to get actors name
      request(actors[i], (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const actorsInfo = JSON.parse(body);
          console.log(actorsInfo.name);
        }
      });
    }
  }
});
// get characters in the season from the above response
