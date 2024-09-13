// Link: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript#private_methods
class Example {
  somePublicMethod() {
    this.#somePrivateMethod();
  }

  #somePrivateMethod() {
    console.log("You called me?");
  }
}

const myExample = new Example();
myExample.somePublicMethod(); // 'You called me?'
myExample.#somePrivateMethod(); // SyntaxError
