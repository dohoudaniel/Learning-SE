// I wrote this code myself.
#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (process.argv.length === 3) {
  console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : arg1 + ' is ' + undefined);
} else {
  console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : arg1 + ' is ' + arg2);
}
