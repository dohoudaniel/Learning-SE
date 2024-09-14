/**
 * This calculator was built using NodeJS.
 * It handles four (4) basic iperations.
 * - Addition
 * - Subtraction
 * - Division
 * - Multiplication
 */

// Defining variables
let username;
let num1;
let num2;
let operator;

// Include the readline module to handle command line inputs
const readline = require('readline');

// Creating a readline interface using stdin for input and stdout for output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Store user's username
rl.question('Enter your username: ', (username) => {
  // Storing username and delaying the printing of username
  setTimeout(() => {
    console.log(`Welcome, ${username.}`);
  }, 2000);
  rl.close();
});
console.log();

// Print 'Welcome Message' to standard output
setTimeout(() => {
  console.log('Thank you for using this calculator.');
}, 2000);
console.log();
setTimeout(() => {
  console.log('This is a basic calculator that handles:');
}, 2000);
setTimeout(() => {
  console.log('Addition: +');
}, 2000);
setTimeout(() => {
  console.log('Subtraction: -');
}, 2000);
setTimeout(() => {
  console.log('Multiplication: *');
}, 2000);
setTimeout(() => {
  console.log('Division: /');
}, 2000);
console.log();
setTimeout(() => {
  console.log('You need to enter two numbers and an arithmeti operator as listed above.');
}, 2000);
console.log();
setTimeout(() => {
  console.log('Calculator started...');
}, 2000);
console.log();
console.log();

// Prompt the user for two numbers and an arithmetic operator
rl.question('Enter your first number: ', (num1) => {
  // Validating the first number from user stdin
  if (isNaN(num1)) {
    console.log('Error: Invalid Input.\nYou need to enter a valid number.\nTry again!.');
    rl.close(); // Terminating stdin
  } else {
    setTimeout(() => {
      console.log('Number validated.');
    }, 2000);
    rl.close();
  }
  console.log();

  // Second number
  rl.question('Enter your second number: ', (num2) => {
    // Validating the second number from user stdin
    if (isNaN(num2)) {
      console.log('Error: Invalid Input.\nYou need to enter a valid number.\nTry again!.');
      rl.close();
    } else {
      setTimeout(() => {
        console.log('Number validated.');
      }, 2000);
      rl.close();
    }
    console.log();

    // Arithmetic operator
    rl.question('Enter an arithmetic operator: ', (operator) => {
      // Typecasting before performing an arithmetic operation
      num1 = parseFloat(num1);
      num2 = parseFloat(num2);
      let result;

      // Performing arithmetic operation using a switch statement
      switch (operator) {
        case '+':
          result = num1 + num2;
          break;
        case '-':
          result = num1 - num2;
          break;
        case '*':
          result = num1 * num2;
          break;
        case '/':
          if (num2 !== 0) {
            result = num1 / num2;
          } else {
            console.log('Error: Division by zero. Impossible operation.');
            console.log('Try again.');
            rl.close();
            return;
          }
          break;
        default:
          console.log('Invalid operator entered!\nAccepted operators are + , - , * and /');
          console.log();
          rl.close();
          return;
      }

      // Printing result of arithmetic operation
      setTimeout(() => {
        console.log('Performing arithmetic operation...');
        console.log();
      }, 2500);

      setTimeout(() => {
        console.log('Arithmetic calculation done.');
        console.log();
      }, 2000);

      setTimeout(() => {
        console.log(`Result of arithmetic operation: ${name}.`);
        console.log();
      }, 2000);

      // Printing exit message
      console.log(`Thank you ${username} for using this calculator.\nRun this file to use it again.\nBye ${username}.`);
      rl.close();
    });
  });
});
