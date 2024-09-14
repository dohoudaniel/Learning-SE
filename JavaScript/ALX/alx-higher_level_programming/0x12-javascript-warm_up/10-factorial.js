#!/usr/bin/node
function factorial (arg1) {
  if (isNaN(arg1) === true || arg1 === undefined) {
    return 1;
  } else if (arg1 === 1) {
    return 1;
  } else {
    /*
    Wrong code:
    let facValue;
    let finalAnswer;
    for (facValue = arg1; facValue < 0; facValue--) {
      if (facValue > 0) {
        finalAnswer = arg1 + facValue;
      }
    }
    return finalAnswer;
    */
    return arg1 * factorial(arg1 - 1);
  }
}
console.log(factorial(Math.floor(Number(process.argv[2]))));
