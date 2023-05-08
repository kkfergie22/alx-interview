#!/usr/bin/node
const movieId = process.argv[2]; // get movie ID from command line argument
const apiUrl = `https://swapi.dev/api/films/${movieId}/`; // construct API URL

fetch(apiUrl) // make API request
  .then((response) => response.json()) // parse response as JSON
  .then((data) => {
    // handle response data
    const characters = data.characters; // extract character URLs from response
    characters.forEach((characterUrl) => {
      // loop through character URLs
      fetch(characterUrl) // make API request for each character
        .then((response) => response.json()) // parse response as JSON
        .then((characterData) => {
          // handle response data for each character
          console.log(characterData.name); // print character name
        })
        .catch((error) => console.error(error)); // handle errors
    });
  })
  .catch((error) => console.error(error)); // handle errors
