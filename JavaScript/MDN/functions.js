/*
Functions - MDN
Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions
*/

// Defining functions
function square (number) {
  return number * number;
}
console.log(square(7));

// Parameters and objects in functions
function danielFunc (daniel) {
  daniel.make = 'A';
}

const trials = {
  make: 'The',
  a: 'Beautiful',
  change: 'Mind'
};

// Getting the value of make
const fr = trials.make;
console.log(fr);

// Modifying the make property using a function
danielFunc(trials);
// Getting the value of 'make'
const fret = trials.make;
console.log(fret);

// Passing an array as a parameter to a function
function myFunction (theArray) {
  theArray[0] = 20;
}
// When you pass an array as a parameter,
// if the function changes any of the array's values, that change is visible outside the function.
const arr = [45];
console.log(arr[0]);
myFunction(arr);
console.log(arr[0]);

/* Function Expressions */
// In function expressions, a function can be anonymous; it does not have to have a name. Example:
const division = function (aNumber) {
  return aNumber / aNumber;
};
const x = division(100);
console.log(x);
// However, a name can be provided with a function expression. Providing a name allows the function to refer
//  to itself, and also makes it easier to identify the function in a debugger's stack traces.
const multix = function mult (n) {
  return n * 10;
};
console.log(multix(100)); // Accessing the function through the name of our variable

// ⭐ - Function expressions are convenient when passing a function as an argument to another function.
// The following example shows a 'maps' function that should receive a function as first argument and an
// array as second argument:
function maps (a, b) {
  // The Array() constructor is used to construct Array objects.
  const myResult = new Array(b.length);
  for (let d = 0; d < b.length; d++) {
    myResult[d] = a(b[d]);
  }
  return myResult;
}
// In the following code, the function receives a function defined by a function
// expression and executes it for every element of the array received as a second argument:
function google (g, h) {
  const myResult = new Array(h.length);
  for (let i = 0; i < h.length; i++) {
    myResult[i] = g(h[i]);
  }
  return myResult;
}
// Thanks to JS for Hoisting.
const g = function (x) {
  return x * x * x;
};
const myNumbers = [0, 1, 2, 3, 4, 5];
const cubes = google(g, myNumbers);
console.log(cubes);

// We can also define functions based on conditions
/*
let myFunc
if (num === 0) {
  myFunc = function (theObject) {
    theObject.make = "Toyota"
  }
}
*/

// To be continued...
