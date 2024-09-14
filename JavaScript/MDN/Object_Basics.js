/*
JavaScript Objects
Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics
*/
const person = {
  name: ['Bob', 'Smith'],
  age: 32,
  about: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name}.`);
  }
};
const myName = person.name; // A global variable
const name1 = person.name[0]; // A global variable
const age = person.age; // A global variable
console.log(myName);
console.log(name1);
console.log(age);
person.introduceSelf();
person.about();
console.log();

// You know how to use the dot notation to access object properties and methods.

// Accessing objects as object properties:
const aPerson = {
  name: {
    first: 'Bob',
    last: 'Smith'
  }
};
// To access these items you just need to chain the extra step onto the end with another dot.
console.log(aPerson.name.first);
console.log(aPerson.name.last);
console.log();

/* Bracket Notation */
const anotherPerson = {
  name: {
    first: 'Bob',
    last: 'Smith'
  }
};
// console.log(anotherPerson['name']['first']); // This prints 'Bob'
// console.log(anotherPerson["name"]["last"]); // This prints 'Smith'
// It is better to access properties and objects using dot notation.
console.log(anotherPerson.name.first); // This prints 'Bob'
console.log();
/*
This looks very similar to how you access the items in an array, and it is basically the same thing
— instead of using an index number to select an item, you are using the name associated with each
member's value. It is no wonder that objects are sometimes called associative arrays — they map strings
to values in the same way that arrays map numbers to values.
*/

// Dot notation is generally preferred over bracket notation because it is more succinct and easier to read.
/* ⭐ - However there are some cases where you have to use brackets.
For example, if an object property name is held in a variable, then you can't use dot notation to access the value,
but you can access the value using bracket notation. */
// An example as used in a function:
const daniel = {
  nom: ['Dohou', 'Daniel'],
  age: 16,
  dob: 18052006
};
function logObjectProperties (propertyName) {
  console.log(daniel[propertyName]);
}
logObjectProperties('nom'); // Doing this prints - '[ 'Dohou', 'Daniel' ]'
/*
However, this returns undefined:
function logObjectProperties(propertyName) {
  console.log(daniel.propertyName.)
}
logObjectProperties('nom'); // Doing this prints - 'undefined'
*/
console.log();

// Setting object members
const modify = {
  nom: {
    firstName: 'Danielle',
    lastName: 'Dohou'
  },
  Age: 20,
  dob: 18052006
};
modify.Age = 16;
modify.dob = 'May 18, 2006';
modify['nom']['firstName'] = 'Daniel'; // Using Bracket Notation. Dot notation can be used and is better used here.
console.log(modify);

// Creating new members
modify.bestColor = 'Red';
modify.intro = function () {
  console.log('Hi everyone. My name is ' + this.nom.firstName + '.'); // Using the 'this' keyword.
  console.log('I am ' + modify.Age + ' years old.');
  console.log('I was born on the ' + this.dob + '.'); // Using the 'this' keyword.
  console.log('My best color is ' + modify.bestColor + '.');
};
console.log(modify);
modify.intro();
console.log();

// One useful aspect of bracket notation is that it can be used to set not only member values dynamically,
// but member names too.
const myHeight = 'height';
const myHeightValue = '6 inches';
modify[myHeight] = myHeightValue;
modify.intro();
console.log('I am ' + modify[myHeight] + ' tall.');
console.log(modify);
// console.log(modify.length); => undefined
console.log();

// Introducing Constructors
// 1. Using a function:
function createPerson (name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
  return obj;
}
/*
This function creates and returns a new object each time we call it. The object will have two members:
- a property name
- a method introduceSelf().
*/
// console.log(createPerson('Hyacinth'))
const newPerson = createPerson('Hyacinth');
console.log(newPerson.introduceSelf);

/*
function createPerson (name) {
  this.name = name
  console.log(`Hi! I'm ${this.name}.`)
  return name
}
*/

console.log();

// 2. Using a constructor
/*
A constructor is just a function called using the new keyword.
When you call a constructor, it will:
- create a new object
- bind this to the new object, so you can refer to this in your constructor code
- run the code in the constructor
- return the new object.
*/
// Example:
function Myconstructor (name) {
  this.name = name;
  this.introduction = function () {
    console.log(`Hi. I am ${this.name}.`);
  };
}
// Calling myConstructor as a constructor using the 'new' keyword.
const newObject = new Myconstructor('Barry Allen');
console.log(newObject.name);
newObject.introduction();
