#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
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
