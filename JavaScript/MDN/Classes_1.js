/*
Classes in JavaScript
Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript
*/

/* Classes and Constructors */
class Person {
  name = '';

  /*
  The name; declaration is optional: you could omit it,
  and the line this.name = name; in the constructor will create the name property before initializing it.
  However, listing properties explicitly in the class declaration might make it easier for people reading
  your code to see which properties are part of this class.
  */
  constructor (name) {
    this.name = name;
  }
  /*
  You could also initialize the property to a default value when you declare it, with a line like:
  name = '';
  */

  introduction () {
    console.log(`Hi, I am ${this.name}.`);
  }
}
const daniel = new Person('Daniel');
daniel.introduction();

console.log();

/* Omitting constructors */
// If you don't need to do any special initialization, you can omit the constructor,
// and a default constructor will be generated for you:
class Animal {
  sleep () {
    console.log('zzzzzzzzzzz!');
  }
}
const Jock = new Animal();
Jock.sleep();

/* Inheritance */
// Given our Person class above, let's define the Professor subclass.
class Professor extends Person {
  course;

  constructor (name, course) {
    super(name);
    this.course = course;
  }

  introduction() {
    console.log(`My name is ${this.name}, and I will be your ${this.course} professor.`);
  }

  // The grading function
  grade(paper) {
    const studentGrade = Math.floor(Math.random() * (5 - 1) + 1);
    console.log(studentGrade);
  }
}
/*
We use the extends keyword to say that this class inherits from another class.
The Professor class adds a new property teaches, so we declare that.

Since we want to set teaches when a new Professor is created, we define a constructor,
which takes the name and teaches as arguments. The first thing this constructor does is
call the superclass constructor using super(), passing up the name parameter.
The superclass constructor takes care of setting name. After that, the Professor constructor
sets the teaches property.

Note: If a subclass has any of its own initialization to do, it must first call the superclass constructor
using super(), passing up any parameters that the superclass constructor is expecting.

We've also overridden the introduceSelf() method from the superclass, and added a new method grade(),
to grade a paper (our professor isn't very good, and just assigns random grades to papers).
*/
const george = new Professor('George', 'Space Time  Physics');
george.introduction();
george.grade();

// Dealing with data
/* Data Encapsulation */
/*
Finally, let's see how to implement encapsulation in JavaScript.
In the last article we discussed how we would like to make the year property of Student private,
so we could change the rules about archery classes without breaking any code that uses the Student class.

Here's a declaration of the Student class that does just that:
*/
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
/*
In this class declaration, #year is a private data property.
We can construct a Student object, and it can use #year internally,
but if code outside the object tries to access #year the browser throws an error:
*/
const Chloe = new Student('Chloe', 2);
Chloe.introduceSelf(); // Hi! I'm Summers, and I'm in year 2.
console.log(Chloe.canStudyArchery()); // Prints 'true'
// Chloe.#year; // Returns a SyntaxError

/* Private Methods */
/*
You can have private methods as well as private data properties.
Just like private data properties, their names start with #, and they can only be called by
the object's own methods
*/
class Example {
  somePublicMethod() {
    this.#somePrivateMethod();
  }

  #somePrivateMethod() {
    console.log('You called me?');
  }
}
const myExample = new Example();
myExample.somePublicMethod(); // 'You called me?'
// myExample.#somePrivateMethod(); // Returns a SyntaxError
