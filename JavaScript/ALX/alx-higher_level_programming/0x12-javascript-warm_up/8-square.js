#!/usr/bin/node
const commLineArg = Math.floor(Number(process.argv[2]));
if (isNaN(commLineArg) === true) {
  console.log('Missing size');
} else {
  for (let column = 0; column < commLineArg; column++) {
    let row = '';
    // This line declares another for loop that iterates c from 0 to size - 1, incrementing c
    // by 1 on each iteration. Inside the loop, it appends the character "X" to the row string.
    for (let r = 0; r < commLineArg; r++) row = row + 'X';
    console.log(row);
  }
}
