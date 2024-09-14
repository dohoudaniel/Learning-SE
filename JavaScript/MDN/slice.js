// The slice() method
// Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice
/*
The slice() method returns a shallow copy of a portion of an array into a new array object selected
from start to end (end not included) where start and end represent the index of items in that array.
The original array will not be modified
*/
const daniel = ['I', 'Am', 'A', 'Beautiful', 'Mind', 'And', 'I', 'Am', 'The', 'Flash'];
console.log(daniel.slice(2)); // Output: [ 'A', 'Beautiful', 'Mind', 'And', 'I', 'Am', 'The', 'Flash' ]
console.log(daniel.slice(2, 4)); // Output: [ 'A', 'Beautiful' ]
console.log(daniel.slice(2, 5)); // Output: [ 'A', 'Beautiful', 'Mind' ]
console.log(daniel.slice(-2)); // Output: [ 'The', 'Flash' ]
console.log(daniel.slice());

/*
Syntax:  slice();
        slice(start);
        slice(start, end);
*/
