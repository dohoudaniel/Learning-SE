// console.log('Hello, World');
const myVariable = 'Bob';
console.log(myVariable);

const iceCream = 'chocolate';
if (iceCream === 'chocolate') {
  console.log('Yay, I love chocolate ice cream!');
} else {
  console.log('Awwww, but chocolate is my favorite…');
}

const dog = { name: 'Spot', breed: 'Dalmatian' };
console.log(dog.name);

const foo = 42; // foo is a number
const result = foo + '1'; // JavaScript coerces foo to a string, so it can be concatenated with the other operand
console.log(result); // 421
console.log(typeof (foo));
console.log(typeof null); // Returns 'object'

// Testing the strict equality sign
console.log(typeof null === 'object');
