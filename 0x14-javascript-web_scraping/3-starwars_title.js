#!/usr/bin/node
const request = require('request');
const headers = {
  url: `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  method: 'GET'
};
request(headers, (e, r, d) => {
  console.log(JSON.parse(d).title);
});
