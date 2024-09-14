/**
 * Explanation on how to use the parseInt () in JS
 */
// Example:
const myString = '555';
const myInt = parseInt(myString);
console.log(myInt);
console.log(typeof myInt);

// The `parseInt` function in JavaScript is used to convert a string representation of an integer to an actual
// integer value. It takes two arguments: the string that represents the integer, and an optional radix or base that
// specifies the numerical base for parsing the string. The syntax for `parseInt` is as follows:

// javascript
// --> parseInt(string, radix)

// The `string` argument is the string that represents the integer you want to parse. It can contain numeric
// characters (0-9) and an optional sign (+ or -) at the beginning.

// The `radix` argument is optional and specifies the base for parsing the string. It can be an integer
// value between 2 and 36, where 10 represents the decimal (base-10) system, and other values represent different numerical bases. If `radix` is not provided, `parseInt` assumes base-10 as the default.

// Here's an example of using `parseInt` to convert a string to an integer:

// javascript
const str1 = '123'; // a string representation of an integer
const num1 = parseInt(str1); // converts "123" to 123 (base-10)
console.log(num1); // Output: 123

const str2 = '1010'; // a string representation of a binary number
const num2 = parseInt(str2, 2); // converts "1010" to 10 (base-2)
console.log(num2); // Output: 10

const str3 = '1A'; // a string representation of a hexadecimal number
const num3 = parseInt(str3, 16); // converts "1A" to 26 (base-16)
console.log(num3); // Output: 26

// Note that `parseInt` only parses the string until the first invalid character is encountered.
// It stops parsing when it encounters a character that is not a valid digit in the specified radix.
// Also, `parseInt` returns `NaN` (Not a Number) if the string cannot be parsed into a valid integer.
// It's important to handle this case in your code accordingly.
