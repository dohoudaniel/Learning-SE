#!/usr/bin/node
module.exports = class Rectangle {
  /* My code */
  constructor (w, h) {
    if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
      return 'Rectangle {}'; // Clever 😅
    }
    this.width = w;
    this.height = h;
  }
};
