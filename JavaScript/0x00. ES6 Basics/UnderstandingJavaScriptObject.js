// Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics
// An empty object declaration
const myObject = {};
console.log(myObject); // Returns '{}'
console.log(typeof (myObject)); // Returns 'Object

console.log();

// Declaring values to an object
const anotherObject = {
  name: ['A', 'Beautiful', 'Mind'],
  person: {
    firstName: 'Daniel',
    lastName: 'Dohou',
    middleName: 'Favour'
  },
  age: 2022,
  calls: function () {
    console.log(`${this.name[0]} ${this.name[1]} ${this.name[2]} was born in ${this.age}`);
    return 'Strings';
  }
};

// console.log(anotherObject);

// Printing the values of anotherObject using dot notation
console.log(anotherObject.age);
console.log(anotherObject.name);
anotherObject.calls();
console.log(anotherObject.person.firstName);
console.log(anotherObject.person.lastName);
console.log(anotherObject.person.middleName);

console.log();

// Printing values using bracket notation
console.log(anotherObject['age']);
console.log(anotherObject['name']);
console.log(anotherObject['person']['firstName']);
console.log(anotherObject['person']['lastName']);
console.log(anotherObject['person']['middleName']);

console.log();

// Setting object members
anotherObject.age = 2024;
console.log(anotherObject.age);
// Creating new members in an object too
anotherObject.strings = 'Aetheris';
console.log(anotherObject);
console.log('New object added!');

console.log();

/* ===== An inefficient way of creating a function object ===== */
function createPerson (name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
  return obj;
}
const salva = createPerson('Salva');
salva.introduceSelf(); // "Hi! I'm Salva."
const frankie = createPerson('Frankie');
frankie.introduceSelf(); // "Hi! I'm Frankie."

console.log();

/* ===== A more efficient way of creating a function object ===== */
function Person (name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}
const daniel = new Person('Daniel');
// console.log(typeof (daniel)); Returns 'object'
daniel.introduceSelf(); // "Hi! I'm Daniel."
