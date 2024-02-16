#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code', response.statusCode);
  } else {
    try {
      const characters = JSON.parse(body).characters;
      const promises = [];
      for (const char of characters) {
        promises.push(
          new Promise(function (resolve, reject) {
            request(char, (err, res, bd) => {
              if (err) {
                console.error('Error:', err);
              } else if (res.statusCode !== 200) {
                console.error('Error: Unexpected status code', res.statusCode);
              } else {
                resolve(JSON.parse(bd).name);
              }
            });
          })
        );
      }
      Promise.all(promises).then((a) => {
        for (const name of a) {
          console.log(name);
        }
      });
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
