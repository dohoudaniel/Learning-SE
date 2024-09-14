#!/usr/bin/node
const commLineArg = Math.floor(Number(process.argv[2]));
const myArray = ['C is fun'];
let printStatement = '';
if (isNaN(commLineArg) === true) {
  console.log('Missing number of occurrences');
} else {
  let d; // We will use this to print in our loops
  for (d = 0; d < commLineArg; d++) {
    for (printStatement of myArray) {
      console.log(printStatement);
    }
  }
}
