// Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters
// The rest syntax allows a function to accept an indefinite number of arguments as an array
function myFun (a, b, ...manyMoreArgs) {
  console.log('a', a);
  console.log('b', b);
  console.log('manyMoreArgs', manyMoreArgs);
}

myFun('one', 'two', 'three', 'four', 'five', 'six');

// Console Output:
// a, one
// b, two
// manyMoreArgs, ["three", "four", "five", "six"]
//
//
//
// Link: https://www.w3schools.com/js/js_iterables.asp
// Home Made Iterables
// Home Made Iterable
function myNumbers () {
  let n = 0;
  return {
    next: function () {
      n += 10;
      return { value: n, done: false };
    }
  };
}
// Create Iterable
const n = myNumbers();
console.log(n.next()); // Returns 10
console.log(n.next()); // Returns 20
console.log(n.next()); // Returns 30
