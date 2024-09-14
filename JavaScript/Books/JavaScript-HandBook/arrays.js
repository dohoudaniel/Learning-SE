/*
The JavaScript Handbook
*/
// Arrays
// An array is a collection of elements. Arrays in JavaScript are not a type on their own.
// Arrays are objects.
// There are two ways to initialize arrays:
// Using the array literal syntax.
const a = [];
// Using the Array builtin function:
const b = Array();

// You can pre-fill the array using this syntax:
const c = [1, 2, 3];
const d = Array.of(1, 2, 3);

// Printing an array
console.log(a);
console.log(b);
console.log(c);
console.log(d);

// An array can definitely hold any values, even values of different types.
const e = ['Flavour', 10, 100, '3', 1034.656];
console.log(e);

// Creating multi-dimensional arrays:
const matrix = [
  [1, 2, 3], // [10, 20, 30],
  [4, 5, 6], // [40, 50, 60],
  [7, 8, 9] // [70, 80, 90],
];
console.log(matrix[0][0]);
console.log(matrix[0][1]);
console.log(matrix[1][1]);
console.log(matrix[2][2]);
// Syntax: console.log(arrayName[row_number][column_name]);

// Indexing an array:
console.log(e[0]);
console.log(matrix[0]);

// Initializing a new array with a set of values
// using the syntax below, which hereby initializes
// an array of 10 elements, and fills each element
// with the '7' number:
const Daniel = Array(12).fill('16');
console.log(Daniel);

// Getting the number of elements in an array by checking its length property
console.log(Daniel.length);

// Note that you can set the length of the array. If you assign a bigger number
// than the array's current capacity, nothing happens. If you assign a smaller
// number, the array is cut at that position:
const lengthArray = [7, 49, 343];
console.log(lengthArray);
console.log(lengthArray.length); // Returns 3.
lengthArray.length = 2; // Nothing happens.
console.log(lengthArray.length); // Returns 2.

// Adding items to an array.
// Adding items to an array to the:
const addItemsToArray = [10, 20, 30, 40, 'Daniel'];
console.log(addItemsToArray);
console.log('Length of addItemsToArray is ' + addItemsToArray.length);

// end of an array using the push() method:
addItemsToArray.push(4);
// The push method New elements to add to the array appends new elements to
// the end of an array, and returns the new length of the array.
console.log(addItemsToArray); // Added 4 to the end of the array
console.log('The new length of addItemsToArray is ' + addItemsToArray.length);

// beginning of an array using the unshift() method
console.log(addItemsToArray);
addItemsToArray.unshift('I', 'Am', 'A', 'Beautiful', 'Mind');
// unshift() - Inserts new elements at the start of an array, and returns the new length of the array.
console.log(addItemsToArray);
console.log('The new length of addItemsToArray is ' + addItemsToArray.length);

// Removing items from an array
// Removing items from an array at:
// the end of the array using the pop() method
const removeItemsFromAnArray = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90];
removeItemsFromAnArray.pop();
// pop() - Removes the last element from an array and returns it.
// If the array is empty, undefined is returned and the array is not modified.

console.log('The array \'removeItemsFromAnArray\' is -> ' + removeItemsFromAnArray);

// the beginning of the array using the shift method:
removeItemsFromAnArray.shift();
// shift() - Removes the first element from an array and returns it.
// If the array is empty, undefined is returned and the array is not modified.
console.log('The array \'removeItemsFromAnArray\' is -> ' + removeItemsFromAnArray);

// Joining two or more arrays:
const rem = [1, 2];
const grep = [3, 4];

// Joining multiple arrays using the concat() method:
const remgrep = rem.concat(grep);
// const remgrep = rem.concat(grep, removeItemsFromAnArray);  # This works.
console.log(remgrep);

// Joining multiple arrays using the spread operator ( ... ) in this way:
const remgrep2 = [...rem, ...grep];
console.log(remgrep2);

/*
if (remgrep !== remgrep2) {
  console.log('true');
  -> Prints true
}
*/

// Finding a specific item in an array using

const trap = [1, 2, 3, 4, 5, 6];
/*
- the find() method.

Syntax: arrayName.find((element, index, array) => {
  # returns true of false
})

This method returns the first item that returns true in the callback function provided.
It returns undefined if nothing returns "true".

Documentation for find() method:
find(predicate: (value: number, index: number, obj: number[]) => value is number, thisArg?: any): number | undefined

If provided, it will be used as the this value for each invocation of predicate.
If it is not provided, undefined is used instead.
Returns the value of the first element in the array where predicate is true, and undefined otherwise.
*/
// Example from MDN:
const drip = trap.find(element => element > 3);
// Returns the first element of the array 'trap' that is greater than 3.
console.log('drip is ' + drip);

/*
- Using the findIndex() method
The findIndex() is another array method that works similarly to find() , but
returns the index of the first item that returns true, and if not found, it
returns undefined.
Syntax -> a.findIndex((element, index, array) => {
  # This is where you define the function
  # return true or false
})
*/
/*
w3schools: the findIndex() method
The findIndex() method executes a function for each array element.
The findIndex() method returns the index (position) of the first element that passes a test.
The findIndex() method returns -1 if no match is found.
The findIndex() method does not execute the function for empty array elements.
The findIndex() method does not change the original array.
Syntax:
    array.findIndex(function(currentValue, index, arr), thisValue)
Parameter       Description
function()    Required.
                A function to be run for each array element.
currentValue  Required.
                The value of the current element.
index         Optional.
                The index of the current element.
arr             Optional.
                The array of the current element.
thisValue     Optional. Default undefined.
                A value passed to the function as its this value.
*/
// Example:
const ages = [3, 10, 18, 20];
function checkAge (age) {
  return age > 18;
}
const beauty = ages.findIndex(checkAge);
console.log('The value of beauty is ' + beauty); // The index of the number greater than 18 (20) -> index 3.

/*
- Using the includes() method
Another useful method is includes() :
Syntax:   a.includes(value)
Returns true if a contains value .

        a.includes(value, i)
Returns true if a contains value after the position i .

Documentation:
The element to search for.
Determines whether an array includes a certain element, returning true or false as appropriate.
*/
const grow = trap.includes(4);
console.log(grow);
const rubble = trap.includes(100);
console.log(rubble);
