/*
The JavaScript Handbook
*/
// Declaration of variables using var, const and let

// There are 2 main ways to declare variables
// Using const: const defines a constant reference to a value.
// This means the reference cannot be changed. You cannot reassign a new value to it.
// Const variables must be initialized at the declaration time:
const a = 0;
// Using let you can assign a new value to it.
let b = 0;
b = 1;
// let values can be initialized later
let m;
m = 2;

console.log('I defined three variables. They are: a, b and m\n');
// You can print a new line by using '\n' too.
console.log('The value of a is ' + a);
console.log('The value of b is ' + b + ' and the value of m is ' + m);

// const does not mean "constant" in the way some other languages like C
// mean. In particular, it does not mean the value cannot change - it means it
// cannot be reassigned.
