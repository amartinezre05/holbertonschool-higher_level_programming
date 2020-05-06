#!/usr/bin/node
const myVar = process.argv;
const myNum = parseInt(myVar[2], 10);
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('X'.repeat(myNum));
  }
}
