// #!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argums = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => a - b);
  console.log(argums[argums.length - 2]);
}

/*
# ChatGPT - Explanation of code:
Hello! This is a JavaScript code that runs on Node.js.
This code takes in command-line arguments and finds the second largest number among them.
- Here's a step-by-step breakdown of how it works:

- The first line #!/usr/bin/node specifies the interpreter that should be used to run this script.
- The if statement checks if there are less than or equal to three command-line arguments
(the first argument is always the path to the script itself).
If there are not enough arguments, it simply logs 0 to the console and exits.
- If there are enough arguments, the else block is executed. First, the process.argv array
(which contains the command-line arguments) is mapped to a
new array of numbers using the Number function.
- The .slice(2, process.argv.length) method is used to remove the first two elements (the script path
and the first argument) and return a new array with the remaining arguments.
- The sort method is then used to sort the array in ascending order. The sort function takes two
arguments a and b which are two numbers to be compared.
If the sort method returns a positive number, it means that b should come before a in the sorted array.
If it returns a negative number, it means that
a should come before b in the sorted array. If it returns 0, it means that the two numbers are equal.
- Finally, the second largest number in the sorted array is logged to the console using the expression
args[args.length - 2].
The expression args.length - 2 is used to access the second last element of the args array, which is the
second largest number.

- I hope that helps! Let me know if you have any questions.
*/

/*
Explanation of the sort((a, b) => a - b)
This is a method of the Array object in JavaScript that sorts the elements of an array in ascending order.

The sort() method takes an optional parameter, which is a function that defines the sort order.
In this case, the function is (a, b) => a - b, which is a shorthand for:

function(a, b) {
  return a - b;
}

This function compares two values a and b and returns a negative number if a should be sorted before b,
a positive number if a should be sorted after b, or zero if a and b are equal.

By default, the sort() method sorts elements as strings, which can lead to unexpected results when sorting
numbers. By using the comparison function (a, b) => a - b, the sort() method sorts the elements numerically
by subtracting b from a. If the result is negative, a is sorted before b. If the result is positive,
a is sorted after b. If the result is zero, a and b are considered equal and their order is not changed.
*/
