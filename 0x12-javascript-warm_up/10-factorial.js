#!/usr/bin/node
const myVar = process.argv;
const myNum = parseInt(myVar[2], 10);

function factorial (n) {
  if (n > 0) {
    return n * factorial(n - 1);
  } else {
    return 1;
  }
}
console.log(factorial(myNum));
