#!/usr/bin/node
exports.callMeMoby = function (num, myFunction) {
  let dan;
  for (dan = 0; dan < num; dan++) {
    myFunction();
  }
};
