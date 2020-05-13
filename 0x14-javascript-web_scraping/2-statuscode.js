#!/usr/bin/node
const request = require('request');
request(process.argv[2], (e, r, d) => {
  console.log('code: %d', r.statusCode);
});
