#!/usr/bin/node
const request = require('request');

const id = process.argv.slice(2);
const url = `https://swapi.dev/api/films/${id}`;

const starWars = async () => {
  try {
    const body = await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });

    const res = JSON.parse(body);

    for (const characterUrl of res.characters) {
      const body = await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(body);
          }
        });
      });

      try {
        const res = JSON.parse(body);
        console.log(res.name);
      } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
      }
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

starWars();
