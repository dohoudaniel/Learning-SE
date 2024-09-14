/* MDN Tests - Objects */
// Task 1
/*
Question
--------
In this task you are provided with an object literal, and your tasks are to:
- Store the value of the name property inside the catName variable, using bracket notation.
- Run the greeting() method using dot notation (it will log the greeting to the browser's console).
- Update the color property value to black.
*/

// Solution
const cat = {
  name: 'Bertie',
  breed: 'Cymric',
  color: 'white',
  greeting: function () {
    console.log('Meow!');
  }
};

// Put your code here
const catName = cat['name'];
cat.greeting();
cat.color = 'black';

/* **** I wrote this **** */
console.log(`The cat's name is ${catName}.`);
cat.greeting();
console.log(`The cat's color is ${cat.color}.`);

// Don't edit the code below here
/*
let para1 = document.createElement('p');
let para2 = document.createElement('p');

para1.textContent = `The cat's name is ${ catName }.`;
para2.textContent = `The cat's color is ${ cat.color }.`;

section.appendChild(para1);
section.appendChild(para2);
*/
