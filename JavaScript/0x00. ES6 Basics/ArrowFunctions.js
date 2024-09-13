// Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
// This arrow function returns the length of the values of the array
// const materials = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium'];
// console.log(materials.map((material) => material.length)); // Output: Array [8, 6, 7, 9]
// console.log();
//
// A traditional anonymous function
// (function (a) {
//   return a + 100;
// });
// Remove the 'function' keyword, and place an arrow between the argument and opening body brace
// (a) {
//   return a + 100;
// };
// Next, remove the body braces, and the 'return' keyword
// (a) => a + 100;
// Finally, Remove the parameter's parentheses i.e a's parentheses
// a => a + 100; // This is an example of an arrow function
// console.log();
// "use strict";
const obj = {
  i: 10,
  b: () => console.log(this.i, this),
  c () {
    console.log(this.i, this);
  }
};
obj.b(); // logs undefined, Window { /* … */ } (or the global object)
obj.c(); // logs 10, Object { /* … */ }
