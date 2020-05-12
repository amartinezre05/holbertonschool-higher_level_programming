#!/usr/bin/node
const baseSquare = require('./5-square');
class Square extends baseSquare {
  charPrint (c) {
    const myVar = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(myVar.repeat(this.width));
    }
  }
}
module.exports = Square;
