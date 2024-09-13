// Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript
/* Classes In JavaScript */
class Person {
  name; // optional, A name property

  constructor(name) {
    this.name = name;
    // a constructor that takes a 'name' parameter that is used to initialize the new object's name property
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}`);
    // an introduceSelf() method that can refer to the object's properties using this.
  }
}

const daniel = new Person('Daniel');
console.log(daniel.name);
daniel.introduceSelf();


// Omitting Constructors
class Animal {
  sleep() {
    console.log("zzzzzzz!");
  }
}
const spot = new Animal();
spot.sleep(); // 'zzzzzzz'
