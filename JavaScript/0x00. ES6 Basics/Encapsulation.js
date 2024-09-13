// Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript#encapsulation
class Person {
  name;

  constructor(name) {
    this.name = name;
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}`);
  }
}

// Inheriting from the Person class, and using private fields (encapsulation)
class Student extends Person {
  #year;

  constructor(name, year) {
    super(name);
    this.#year = year;
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}, and I'm in year ${this.#year}.`);
  }

  canStudyArchery() {
    return this.#year > 1;
  }
}
const summers = new Student("Summers", 2);
summers.introduceSelf(); // Hi! I'm Summers, and I'm in year 2.
summers.canStudyArchery(); // true
console.log(summers.#year); // SyntaxError
