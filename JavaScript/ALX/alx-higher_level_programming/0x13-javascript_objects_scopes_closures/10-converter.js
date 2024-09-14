#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    return num.toString(base); // Returns a string representation of an object
  };
};
/*
Explanation:
- The converter function takes a base as an argument and returns another function that can be used to convert numbers to the specified base.
- The returned function takes a number (num) as an argument and uses the toString method with the base argument to convert the number to the
specified base.
- The toString method (as used in this context) in JavaScript is used to convert a number to a string representation in a given base.
The base parameter can be any integer between 2 and 36, where 10 represents base 10 (decimal), 2 represents base 2 (binary),
8 represents base 8 (octal), and so on.
*/
