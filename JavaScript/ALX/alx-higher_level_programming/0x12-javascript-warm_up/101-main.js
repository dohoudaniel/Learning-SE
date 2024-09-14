#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
/* The hint here is that the function prints 'C is fun' to the console, but this happens when we call this anonymous function in a for loop in the 101-call_me_moby file. */
