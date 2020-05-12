#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let myVar = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      myVar = myVar + 1;
    }
  }
  return myVar;
};
