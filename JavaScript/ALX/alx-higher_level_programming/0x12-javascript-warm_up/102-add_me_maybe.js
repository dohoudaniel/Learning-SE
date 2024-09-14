#!/usr/bin/node
exports.addMeMaybe = function (num, myFunction) {
  // myFunction.nb = num;
  myFunction(++num);
};
