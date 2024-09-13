// Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes
// An Object Literal
const myObject = {
  city: 'Madrid',
  greet () {
    console.log(`Greetings from ${this.city}`);
  }
};
console.log(myObject.greet()); // 'Greetings from Madrid', returns 'undefined'
console.log();
console.log(Object.getPrototypeOf(myObject)); // [Object: null prototype] {}
console.log();

//
// An Object Constructor
const myOtherDate = new Date();
let object = myOtherDate;
do {
  object = Object.getPrototypeOf(object);
  console.log(object);
} while (object);
// Date.prototype
// [Object: null prototype] {}
// null

console.log();

//
// Shadowing Properties
const myDate = new Date(1995, 11, 17);
console.log(myDate.getTime()); // 819154800000 (this value changes)
myDate.getTime = function () {
  console.log('something else!');
};
myDate.getTime(); // 'something else!'
// This has changed the behavior of the getTime method for this specific instance of the Date object.
// The original method is still available on the prototype.

console.log();

//
// Setting a prototype
// Two ways: Object.create() and `constructors`
// Using Object.create()
const firstPersonPrototype = {
  greet () {
    console.log('hello!');
  }
};
const carl = Object.create(firstPersonPrototype);
carl.greet(); // hello!
// Here we create an object personPrototype, which has a greet() method.
// We then use Object.create() to create a new object with personPrototype as its prototype.
//
// Using constructors
const secondPersonPrototype = {
  greet () {
    console.log(`hello, my name is ${this.name}!`);
  }
};
function Person (name) {
  this.name = name;
}
Object.assign(Person.prototype, secondPersonPrototype); // or Person.prototype.greet = personPrototype.greet;
const john = new Person('John');
john.greet(); // hello, my name is John!
console.log();
// Checking if an object has its own property
const irma = new Person('Irma');
console.log(Object.hasOwn(irma, 'name')); // true, since `this.name = name;` directly assigns name to the `irma` object
console.log(Object.hasOwn(irma, 'greet')); // false, since the greet method is defined on Person.prototype, not directly on the irma object.
console.log();
