#!/usr/bin/node
const request = require('request');

const id = process.argv.slice(2);
const url = `https://swapi.dev/api/films/${id}`;

const func = async () => {
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

    const jsonRes = JSON.parse(body);

    for (const characterUrl of jsonRes.characters) {
      const body2 = await new Promise((resolve, reject) => {
        request(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(body);
          }
        });
      });

      try {
        const jres = JSON.parse(body2);
        console.log(jres.name);
      } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
      }
    }
  } catch (err) {
    console.error('Error:', err);
  }
};

func();
