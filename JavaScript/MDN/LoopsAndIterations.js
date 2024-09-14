/*
Loops and Iteration
*/
// Example:
for (let step = 0; step < 5; step++) {
  // Runs 5 times, with values of step 0 through 4.
  console.log('Walking east one step');
}
console.log();

/*
for (initialization; condition; afterthought) {
  statement
}
*/
function countSelected (selectedObject) {
  // let numberSelected = 0;
  for (let i = 0; i < selectedObject; i++) {
    if (selectedObject <= 10) {
      // numberSelected++;
      console.log('I am A Beautiful Mind!');
    }
  }
}
countSelected(9);
console.log();

/**
do
  statement
while (condition);
*/
let daniel = 20;
do {
  daniel += 1;
  console.log('daniel has a value of ' + daniel);
} while (daniel < 27);
console.log();

/*
while (condition) {
  statement
}
*/
let woman = 0;
let man = 0;
while (man < 10) {
  man++;
  console.log('The value of man is ' + man);
  woman += man;
  console.log('woman has the value of ' + woman);
  // break;
}
console.log('The value of man after the loop is ' + man);
console.log('The value of man after the loop is ' + woman);
console.log(); // This prints a new line.

/*
for...in statement
*/
// using for...in loops for arrays
const statementArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
let variable = 0;
for (variable in statementArray) {
  console.log('The value of variable is ' + variable);
  variable++;
}
console.log();

// for...of statement
/*
The for...of statement creates a loop Iterating over iterable
objects (including Array, Map, Set, arguments object and so on),
invoking a custom iteration hook with statements to be executed
for the value of each distinct property.

Syntax:
        for (variable of object) {
          statement
        }
*/
const myArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
myArray.foo = 'Hello, World!';
console.log('The value of myArray is ' + myArray);

// for...in
for (const i in myArray) {
  console.log('The value of i is ' + i);
}

console.log();

// for...of
for (const j of myArray) {
  console.log('The value of j is ' + j);
}
console.log();
