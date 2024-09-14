#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const H = this.height;
    const W = this.width;
    for (let dan = 0; dan < H; dan++) {
      let char = '';
      for (let fav = 0; fav < W; fav++) {
        // console.log('X');
        // process.stdout.write('X');
        char = char + 'X';
      }
      console.log(char);
    }
  }
};

// To print something to standard output without a new line, use process.stdout.write().
// This just prints the characters to stdout as they are.
// process.stdout.write('Dohou Daniel ');
// process.stdout.write('A Beautiful Mind.');
