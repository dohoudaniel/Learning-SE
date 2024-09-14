/* Object 4 */
// Task 4
/*
Question:
---------
In the code you wrote for Task 3, the greeting() method is defined twice, once for each cat.
This isn't ideal (specifically, it violates a principle in programming sometimes called DRY or
"Don't Repeat Yourself").

In this task we want you to improve the code so greeting() is only defined once, and every cat
instance gets its own greeting() method. Hint: you should use a JavaScript constructor to create cat instances.
Try updating the live code below to recreate the finished example:
*/

function CatInstance (catname, breed) {
  this.catname = catname;
  this.breed = breed;
  // this.color = 'white',
  this.greeting = function () {
    console.log(`Hello, said ${this.catname} the ${this.breed}.`);
  };
}

const myCatInstance = new CatInstance('Jock', 'Bulldog');
myCatInstance.greeting();

const myCatInstance2 = new CatInstance('Husky', 'Russian Wolf');
myCatInstance2.greeting();
