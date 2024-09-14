/*
Classes - JavaScript
Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/
*/
/* Description */
/*
Defining Classes
----------------

class Rectangle {
  constructor (height, width) {
    this.height = height;
    this.width = width;
  }
}

// Expression; the class is anonymous but assigned to a variable
const myRectangle =
class {
  constructor (height, width) {
    this.height = height;
    this.width = width;
  }
};

// Expression; the class has its own name
const ARectangle = class Rectangle2 {
  constructor (height, width) {
    this.height = height;
    this.width = width;
  }
};
*/

// Constructors
/*
The constructor method is a special method for creating and initializing an object created with a class.
There can only be one special method with the name "constructor" in a class — a SyntaxError is thrown
if the class contains more than one occurrence of a constructor method.
*/
class Rectangle {
  constructor (height, width) {
    this.height = height;
    this.width = width;
  }

  /* Methods */

  // Getter
  get area () {
    return this.calcArea();
  }

  // A Method
  calcArea () {
    let Area = 0;
    Area = this.height * this.width;
    return Area;
  }

  * getSides () {
    yield this.height;
    yield this.width;
    yield this.height;
    yield this.width;
  }
}

const mySquare = new Rectangle(10, 10);
console.log(mySquare.area);
console.log([...mySquare.getSides()]); // Prints an array using the * getSides () function.

// Static methods and fields
/*
The static keyword defines a static method or field for a class.
Static properties (fields and methods) are defined on the class itself instead of each instance.
Static methods are often used to create utility functions for an application, whereas static fields
are useful for caches, fixed-configuration, or any other data that don't need to be replicated across instances.
*/
class Point {
  constructor (x, y) {
    this.x = x;
    this.y = y;
  }

  // Static properties are properties that belong to the class itself, rather than to individual instances
  // of the class.

  static displayName = "A Beautiful Mind";

  // static distance (a, b) {
    // const dx = a.x - b.x;
    // const dy = a.y - b.y;
    //return Math.hypot(dx, dy);
    /*
    Note on the hypot in JavaScript:
    Values to compute the square root for. If no arguments are passed, the result is +0.
    If there is only one argument, the result is the absolute value.
    If any argument is +Infinity or -Infinity, the result is +Infinity.
    If any argument is NaN, the result is NaN. If all arguments are either +0 or −0, the result is +0.
    Returns the square root of the sum of squares of its arguments.
    */

    // My code
    /*
    ChatGPT's explanation to the code below:
    The second static property is a static method called distance that takes two Point instances as
    arguments a and b. The method calculates the distance between the two points using the Pythagorean
    theorem, which is the square root of the sum of the squares of the differences in the x and y coordinates.
    However, in this code, the method is not actually using this calculation, but simply returns the product of
    the x and y coordinates of the first point.
    */
  static distance (a, b) {
    const product = a.x * b.y;
    return product;
  }
}
const p1 = new Point(5, 5); // p1 = (5(x1), 5(y1))
const p2 = new Point(10, 10); // p2 = (10(x2), 10(y2))

console.log(p1.displayName); // undefined
console.log(p1.distance); // undefined
console.log(p2.displayName); // undefined
console.log(p2.distance); // undefined

console.log(Point.displayName); // Prints 'A Beautiful Mind'.
// console.log(Point.distance(p1, p2)); // Prints '7.0710678118654755'
console.log(Point.distance(p1, p2)); // Prints '50'

/*
Code and explanation:

// Code
class Point {
  constructor (x, y) {
    this.x = x;
    this.y = y;
  }

  static displayName = "A Beautiful Mind";

  static distance (a, b) {
    const product = a.x * b.y;
    return product;
  }
}
const p1 = new Point(5, 5);
const p2 = new Point(10, 10);

console.log(p1.displayName); // undefined
console.log(p1.distance); // undefined
console.log(p2.displayName); // undefined
console.log(p2.distance); // undefined

console.log(Point.displayName); // Prints 'A Beautiful Mind'.
console.log(Point.distance(p1, p2));

// ChatGPT's Explanation:
First, a new class called Point is defined using the class keyword. The class has a constructor that
takes two parameters x and y which are used to initialize the x and y properties of the new Point instance:

class Point {
  constructor (x, y) {
    this.x = x;
    this.y = y;
  }


Next, two static properties are defined on the Point class. The first is a static property called displayName
that is set to the string "A Beautiful Mind". Static properties are properties that belong to the class itself,
rather than to individual instances of the class:

  static displayName = "A Beautiful Mind";


The second static property is a static method called distance that takes two Point instances as arguments a and b.
The method calculates the distance between the two points using the Pythagorean theorem, which is the square root
of the sum of the squares of the differences in the x and y coordinates. However, in this code, the method is not
actually using this calculation, but simply returns the product of the x and y coordinates of the first point:

  static distance (a, b) {
    const product = a.x * b.y;
    return product;
  }


After defining the Point class, two new instances of the Point class are created using the new keyword, and assigned
to the variables p1 and p2:

const p1 = new Point(5, 5);
const p2 = new Point(10, 10);


Finally, console.log statements are used to print the values of various properties of the p1, p2,
and Point objects to the console.

console.log(p1.displayName); // undefined
console.log(p1.distance); // undefined
console.log(p2.displayName); // undefined
console.log(p2.distance); // undefined
console.log(Point.displayName); // Prints 'A Beautiful Mind'.
console.log(Point.distance(p1, p2)); // Prints the product of the x and y coordinates of p1.


I hope this explanation helps you! Let me know if you have any more questions.
*/

/* Field Declarations */
// With the class field declaration syntax, the constructor example can be written as:
class Rectangle2 {
  height = 0;
  width;
  constructor (height, width) {
    this.height = height;
    this.width = width;
  }
}

/* Private class features */
class Rectangle3 {
  #height = 0;
  #width;
  constructor(height, width) {
    this.#height = height;
    this.#width = width;
  }
}
/* It's an error to reference private fields from outside of the class; they can only be read or written
within the class body. By defining things that are not visible outside of the class, you ensure that your
classes' users can't depend on internals, which may change from version to version. */

/* Inheritance */
// The extends keyword is used in class declarations or class expressions to create a class as a child of
// another constructor (either a class or a function).
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name); // call the super class constructor and pass in the name parameter
  }

  speak() {
    // super.speak(); -> This is how you call the speak () method from the super class.
    console.log(`${this.name} barks.`);
  }
}
const d = new Dog("Mitzie");
d.speak(); // Mitzie barks.

console.log();

// If there is a constructor present in the subclass, it needs to first call super() before using this.
// The super keyword can also be used to call corresponding methods of super class.
class Cat {
  constructor (name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} is a cat!`);
  }
}
class Lion extends Cat {
  speak() {
    super.speak();
    console.log(`${this.name} roars, because ${this.name} is a lion.`);
  }
}
const lion = new Lion('Simba');
lion.speak();

/* Examples */
// Binding this with instance and static methods
class anAnimal {
  speak () {
    // console.log('I am the Flash');
    return this
  }
  static eat() {
    // console.log('A Beautiful Mind.');
    return this;
  }
}
const obj = new anAnimal();
obj.speak(); // the anAnimal object
const speak = obj.speak;
speak(); // undefined

anAnimal.eat(); // class anAnimal
const eat = anAnimal.eat;
eat(); // undefined


/* If we rewrite the above using traditional function-based syntax in non–strict mode,
then this method calls are automatically bound to globalThis. In strict mode, the value
of this remains as undefined. */
function myAnimal () {}

myAnimal.prototype.speak = function () {
  return this
}

myAnimal.eat = function () {
  return this;
}

const anObject = new myAnimal();
const asApeak = anObject.speak;
asApeak(); // a global object (in strict mode)

const asIEat  = myAnimal.eat;
asIEat(); // global object (in non-strict mode)
