/* JavaScript - Object Prototypes */
// Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

// Creating an object literal
const myObject = {
  city: 'Madrid',
  greet () {
    console.log(`Greetings from ${this.city}.`);
  }
};

myObject.greet();
// myObject.toSting();

// More examples:

// Date is defined in lib.es2020.date.d.ts file in VSCode

const myDate = new Date();
let object = myDate;

do {
  object = Object.getPrototypeOf(object);
  console.log(object);
} while (object);

// Date.prototype
// Object { }
// null

// Shadowing properties
// Date - creates a new date.
const myNewDate = new Date(1995, 11, 17);
console.log(myNewDate.getYear()); // Prints '95'.
myNewDate.getYear = function () {
  console.log('Something else.');
};
myNewDate.getYear();

/* Setting a prototype */
// Using Object.create
