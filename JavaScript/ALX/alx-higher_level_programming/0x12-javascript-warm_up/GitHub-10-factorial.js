#!/usr/bin/node
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}
console.log(factorial(Number(process.argv[2])));

/*
Explanation of code:

Explanation 1:
This is a function that calculates the factorial of a number using recursion.
It takes a single argument n which is the number whose factorial is to be calculated.
The function first checks if the number n is 0 or NaN (not a number). If n is 0 or NaN,
it returns 1. If n is not 0 or NaN, it recursively calls the factorial function with the
argument n - 1, until it reaches the base case of n = 0. The function then multiplies the
result of the recursive call with n to get the factorial of n.

Explanation 2:
This is a function called factorial that takes a single argument n.
The function calculates the factorial of n using recursion. The return
statement checks if n is equal to 0 or is not a number (using the isNaN() function).
If either condition is true, the function returns 1. Otherwise, it calculates the
factorial recursively by multiplying n with the factorial of n - 1
*/
