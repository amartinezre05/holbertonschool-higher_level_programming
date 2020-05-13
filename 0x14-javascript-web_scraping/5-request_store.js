#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], (e, r, d) => {
  fs.appendFile(process.argv[3], d, 'utf-8', (e) => {
    if (e) throw e;
  });
});
