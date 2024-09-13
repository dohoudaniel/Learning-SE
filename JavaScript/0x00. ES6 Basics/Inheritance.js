// Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript#inheritance
class Person {
  name;

  constructor(name) {
    this.name = name;
  }

  introduceSelf() {
    console.log(`Hi! I'm ${this.name}`);
  }
}

// Inheriting from the Person class
class Professor extends Person {
  teaches;

  constructor(name, teaches) {
    super(name);
    this.teaches = teaches;
  }

  introduceSelf() {
    console.log(
      `My name is ${this.name}, and I will be your ${this.teaches} professor.`,
    );
  }

  grade(paper) {
    const grade = Math.floor(Math.random() * (5 - 1) + 1);
    console.log(grade);
  }
}
const walsh = new Professor("Barry Allen", "Physics");
walsh.introduceSelf(); // 'My name is Walsh, and I will be your Psychology professor'
walsh.grade("my paper"); // some random grade
