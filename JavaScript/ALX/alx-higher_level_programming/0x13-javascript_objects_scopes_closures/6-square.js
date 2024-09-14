#!/usr/bin/node
// 'use strict';
const mySquare = require('./5-square.js');
module.exports = class Square extends mySquare {
  /*
  constructor () {
    super();
  }
  */

  charPrint (c) {
    /* if (arguments[0] === undefined) { super.print (); } */
    const H = this.height;
    const W = this.width;
    if (c === undefined) {
      for (let dan = 0; dan < H; dan++) {
        let char = '';
        for (let fav = 0; fav < W; fav++) {
          char = char + 'X';
        }
        console.log(char);
      }
    } else {
      for (let dan = 0; dan < H; dan++) {
        let char = '';
        for (let fav = 0; fav < W; fav++) {
          char = char + c;
        }
        console.log(char);
      }
    }
  }
};
