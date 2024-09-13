// Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
// Lexical Scoping
function init () {
  var name = 'Mozilla'; // name is a local variable created by init
  function displayName () {
    // displayName() is the inner function, that forms the closure
    console.log(name); // use variable declared in the parent function
  }
  displayName();
}
init();

console.log();

// Scoping with curly braces (blocks), using 'var', before 'ES6'
// if (Math.random() > 0.5) {
//   var x = 1;
// } else {
//   var x = 2;
// }
// console.log(x);
// console.log();
//
// Scoping with curly braces (blocks), using 'const', before 'ES6'
// if (Math.random() > 0.5) {
//   const x = 1;
// } else {
//   const x = 2;
// }
// console.log(x); // ReferenceError: x is not defined
// console.log();

// Function scope

// Global scope

// Closures
// function makeFunc () {
//   const name = 'Mozilla';
//   function displayName () {
//     console.log(name);
//   }
//   return displayName;
// }
// const myFunc = makeFunc();
// myFunc();
//
function makeAdder (x) {
  return function (y) {
    return x + y;
  };
}

const add5 = makeAdder(5);
const add10 = makeAdder(10);

console.log(add5(2)); // 7
console.log(add10(2)); // 12

//
console.log();
// Understanding closures using a counter variable
// Initiate a counter
let counter = 0;
// Function to increment counter
function add () {
  counter += 1;
}
// Call add() 3 times
add();
add();
add();
console.log(`counter has the value: ${counter}`); // The counter should now be 3

// Emulation of private methods with closures
