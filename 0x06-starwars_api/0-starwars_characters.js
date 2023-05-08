#!/usr/bin/node
const request = require('request'); // import request package
const movieId = process.argv[2]; // get movie ID from command line argument
const apiUrl = `https://swapi.dev/api/films/${movieId}/`; // construct API URL

request(apiUrl, { json: true }, (err, res, data) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode !== 200) {
    console.error(`Error: ${res.statusCode} - ${res.statusMessage}`);
  } else {
    // handle response data
    const characters = data.characters; // extract character URLs from response
    characters.forEach((characterUrl) => {
      // loop through character URLs
      request(characterUrl, { json: true }, (err, res, characterData) => {
        if (err) {
          console.error(err);
        } else if (res.statusCode !== 200) {
          console.error(`Error: ${res.statusCode} - ${res.statusMessage}`);
        } else {
          // handle response data for each character
          console.log(characterData.name); // print character name
        }
      });
    });
  }
});
