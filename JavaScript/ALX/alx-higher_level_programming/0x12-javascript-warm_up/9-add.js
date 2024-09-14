#!/usr/bin/node
function addArguments (arg1, arg2) {
  if (isNaN(arg1) === true || isNaN(arg2) === true) {
    return NaN;
  } else if (arg1 === undefined) {
    return NaN;
  } else {
    return arg1 + arg2;
  }
}
console.log(addArguments(Math.floor(Number(process.argv[2])), Math.floor(Number(process.argv[3]))));
// I wrote this code 😊😌.
