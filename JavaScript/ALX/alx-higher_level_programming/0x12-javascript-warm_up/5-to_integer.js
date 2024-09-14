#!/usr/bin/node
const arg = Math.floor(Number(process.argv[2]));    // This line converts 'arg' to an integer using the Number() method and rounds it up using the Math.floor() method
if (isNaN(arg) === true) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg}`);
}
