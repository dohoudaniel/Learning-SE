// Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters
// const b = 10;
// const anInteger = typeof (b);
// console.log(anInteger);

function multiply (a, b) {
  b = typeof b !== 'undefined' ? b : 1;
  return a * b;
}

console.log(multiply(5, 2)); // 10
console.log(multiply(5)); // 5

// I'll be stopping here now
