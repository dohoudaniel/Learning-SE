#!/usr/bin/node
function add (a, b) {
  a = Math.floor(Number(a));
  b = Math.floor(Number(b));

  return a + b;
}
exports.add = (a, b) => add(a, b);
