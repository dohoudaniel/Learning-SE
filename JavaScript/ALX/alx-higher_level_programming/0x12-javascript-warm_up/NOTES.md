# Notes taken while doing these tasks:
1. In JavaScript, it is common to access command-line arguments passed to a program using the process.argv array. process.argv[0] is typically the path to the Node.js binary, and process.argv[1] is typically the path to the JavaScript file being executed. Therefore, to access the first argument passed to the JavaScript program, you would use process.argv[2], not process.argv[1].

So, if you are subtracting 2 from some value in your JavaScript program to get the first argument, it could be because you are trying to index the process.argv array with the correct offset to access the first command-line argument passed to your program.

2. In JavaScript, typeof is an operator that returns a string indicating the type of a value or expression. It can be used with any value or expression in JavaScript, and the result will be one of the following string values:
- "undefined": if the value is undefined
- "boolean": if the value is a boolean (true or false)
- "number": if the value is a number (including NaN and Infinity)
- "string": if the value is a string
- "symbol": if the value is a symbol
- "object": if the value is an object (including null, arrays, functions, and objects created with the Object constructor)
- "function": if the value is a function.

3. The map() function
In JavaScript, map() is a higher-order function that is used to transform an array by applying a function to each of its elements and creating a new array with the transformed values. The map() function takes a callback function as its argument, which is executed for each element in the array. The callback function takes three arguments: the current element being processed, its index, and the array being processed.

The syntax for the map() function is as follows:

	array.map(function(currentValue, index, arr) {
	  // function body
	}, thisArg);
- array: the original array that will be transformed
- currentValue: the current element being processed
- index: the index of the current element being processed
- arr: the original array being processed
- thisArg (optional): a value to be passed as this to the function
- The map() function returns a new array with the transformed values.

- Here's an example of using map() to transform an array of numbers by squaring each number:

const numbers = [1, 2, 3, 4, 5];
const squaredNumbers = numbers.map(function(num) {
  return num * num;
});
console.log(squaredNumbers); // [1, 4, 9, 16, 25]
In this example, map() is used to iterate over the numbers array and apply the function num * num to each element. The transformed values are then added to a new array squaredNumbers.
