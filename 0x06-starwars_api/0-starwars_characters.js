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
    // get the characters list in the correct order
    const characters = data.characters;
    const characterUrls = characters.map((characterUrl) => {
      const characterId = characterUrl.match(/\/([0-9]*)\/$/)[1];
      return { url: characterUrl, id: parseInt(characterId) };
    });
    characterUrls.sort((a, b) => a.id - b.id);

    // fetch each character URL in the correct order and print the character name
    characterUrls.forEach((characterUrl) => {
      request(characterUrl.url, { json: true }, (err, res, characterData) => {
        if (err) {
          console.error(err);
        } else if (res.statusCode !== 200) {
          console.error(`Error: ${res.statusCode} - ${res.statusMessage}`);
        } else {
          console.log(characterData.name);
        }
      });
    });
  }
});
