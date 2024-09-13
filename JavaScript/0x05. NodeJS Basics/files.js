// File System Operations
//
// Reading Files
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Writing files
fs.writeFile('example.txt', 'Hello, World!', (err) => {
  if (err) throw err;
  console.log('File has been saved!');
});
