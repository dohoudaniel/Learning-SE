#!/usr/bin/node
exports.esrever = function (list) {
  // The easy way -return list.reverse();

  // Do this the Hard Way!
  // Declaring variables
  const myRevArray = [];
  let myArrObject;
  let arrNum = 0;
  const arrLen = list.length;
  let d;

  for (d = arrLen - 1; d >= 0; d--) {
    myArrObject = list[d];
    myRevArray[arrNum] = myArrObject;
    arrNum++;
  }

  /*
  do {
    myArrObject = list[list.length - 1];
    myRevArray[d] = myArrObject;
    d++;
  } while (arrLen--);
  */

  return myRevArray;
};
