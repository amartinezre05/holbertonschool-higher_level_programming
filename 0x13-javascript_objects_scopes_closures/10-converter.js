#!/usr/bin/node
exports.converter = function (base) {
  return myVar => myVar.toString(base);
};
