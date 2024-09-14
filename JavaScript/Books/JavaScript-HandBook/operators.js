/*
The JavaScript Handbook
*/
// Operators
// The addition operator (+)
const three = 1 + 2;
const Four = three + 1;
const four = 'three' + 1;
console.log(four); // Prints 'three1'
console.log(Four);
// The subtraction operator (-) works the same way.

// The division operator (/)
const division = 140 / 2;
console.log(division);
// If you divide by zero in JS, it does not raise any error. Instead, it returns the Infinity value
const daniel = 40 / 0;
console.log(daniel);

// The remainder operator (%)
const remainder = 20 % 5; // result = 0
const future = 14 % 6; // future = 2
console.log('remainder is ' + remainder + ' and\nfuture is ' + future + '.');
// A remainder by zero is always 'NaN', a special value that means 'Not a Number'
const fan = 100 % 0; // fan is 'NaN'
console.log('The value of fan is ' + fan);

// The multiplication operator (*)
const a = 2 * 3;
console.log('a is equal to ' + a);

// The exponential operator
const flash = 3 ** 2;
console.log('flash = ' + flash);

// Comparison operators
// Comparison operators always return a boolean, i.e a 'true' or a 'false'
const bars = 4;
console.log(bars <= 4); // Prints 'true'

// The equality operators (under comparison operators)
// === -> Checks for equality
// !== -> Checks for inequality.
const growth = 20;
console.log(growth === 20); // Prints 'true'
console.log(growth !== 20); // Prints 'false'
