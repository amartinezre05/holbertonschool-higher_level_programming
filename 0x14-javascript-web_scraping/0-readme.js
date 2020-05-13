#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (e, inp) => {
  if (e) console.log(e);
  else console.log(inp);
});
