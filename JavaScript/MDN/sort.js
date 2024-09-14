/*
The sort() method
*/
// The sort() method sorts the elements of an array in place and returns the reference to the same array,
// now sorted. The default sort order is ascending, built upon converting the elements into strings,
// then comparing their sequences of UTF-16 code units values.
const daniel = ['C', 'Kotlin', 'Python', 'JavaScript'];
daniel.sort();
console.log(daniel);

// Syntax
// Functionless
// sort()

// Arrow function
// sort((a, b) => { /* … */ } )

// Compare function
// sort(compareFn)

// Inline compare function
// sort(function compareFn(a, b) { /* … */ })

// Trying this out
const tryThisOut = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
tryThisOut.sort((a, b) => a - b);
// The code above is not the same as: tryThisOut.sort();
console.log(tryThisOut[tryThisOut.length - 2]);
