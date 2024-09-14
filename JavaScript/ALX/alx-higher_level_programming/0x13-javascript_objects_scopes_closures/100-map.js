#!/usr/bin/node
// Importing the list from 100-data.js
const importList = require('./100-data.js').list;
const newList = importList.map((Item, ItemIndex) => Item * ItemIndex);
console.log(importList);
console.log(newList);

/*

const dan = importList.map(x => x * indexOf(x));
console.log(dan);

const list = [1, 2, 3, 4, 5];
list.map((x, y) => console.log(`The index of ${x} is ${y}`));

const newList = importList.map((x, index) => {
  console.log(index);
  return x * index;
});
console.log(newList);

*/
