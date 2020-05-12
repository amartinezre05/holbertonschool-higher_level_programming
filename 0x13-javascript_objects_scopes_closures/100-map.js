#!/usr/bin/node
const ent = require('./100-data').list;
const out = ent.map((e, idx) => e * idx);
console.log(ent);
console.log(out);
