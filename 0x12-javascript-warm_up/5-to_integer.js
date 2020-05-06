#!/usr/bin/node
const myVar = process.argv;
const myNum = parseInt(myVar[2], 10);
if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
