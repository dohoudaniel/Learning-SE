/**
 * Link: https://www.scaler.com/topics/nodejs/module-exports-vs-exports/
 * This file explains by demonstration the difference between
 * modules.exports and exports in Node JS,
 * and also what the module object and the exports object are all about
 */

console.log('The module object being printed...');
console.log(module);
console.log();
console.log('The exports object being printed...');
console.log(exports);

console.log();
console.log();

// Example:
// On the differences between module.exports and exports
exports.sayHello = function () {
  console.log('Hello World!');
};

module.exports.sayThanks = function () {
  console.log('Thank you :)');
};

module.exports.sayBye = function () {
  console.log('Bye!!!');
};

console.log('The module object being printed...');
console.log(module);
console.log();
console.log('The exports object being printed...');
console.log(exports);

console.log();
console.log();

// Using exports and module.exports in the same module
exports.sayHello = 'Hello World!';

function sayThanks () {
  console.log('Thank you :)');
}

module.exports = sayThanks;

console.log('The module object being printed...');
console.log(module);
console.log();
console.log('The exports object being printed...');
console.log(exports);

/*
Jottings:
- Modules are encapsulated blocks of code that are used in the external application based on its related
functionality.
- ECMAScript 6 (ES6) is the official standard module format for javascript. The filenames have an
extension as .mjs.
- CommonJS is the standard module format for Node.js. The filename has an extension as .js.
- Modules help in reusability, easy maintenance, and easy debugging of code in our application.
- module.exports acts as the object reference that gets returned from the require() calls.
- exports is almost similar to module.exports. It is a reference to module.exports.
- exports is neatly structured code with a better look and is comparatively easy to implement.
- exports supports destructuring assignment, using this we can cherry-pick some particular objects which
we need to import into our application.
- If any object is assigned directly to module. exports, then exports can not be used to export any
object from that module as it no longer refers to module. exports.
*/
