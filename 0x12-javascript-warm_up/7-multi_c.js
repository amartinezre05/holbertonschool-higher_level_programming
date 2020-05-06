#!/usr/bin/node
const myVar = process.argv;
const myNum = parseInt(myVar[2], 10);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
