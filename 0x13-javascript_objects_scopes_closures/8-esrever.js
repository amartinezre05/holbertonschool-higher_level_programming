#!/usr/bin/node
exports.esrever = function (list) {
  const myVar = [];
  for (let i = list.length - 1; i >= 0; i--) {
    myVar.push(list[i]);
  }
  return myVar;
};
