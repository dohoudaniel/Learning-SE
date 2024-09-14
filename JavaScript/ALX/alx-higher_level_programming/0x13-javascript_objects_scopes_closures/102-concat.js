#!/usr/bin/node
// import 'fs';

// The fs module provides file system-related functions, such as reading and writing files
// The fs module enables interacting with the file system in a way modeled on standard POSIX functions.
const fs = require('fs');

// The path module provides utilities for working with file paths.
// const path = require('path');

// Read the files entered as arguments into the command line using fs.readFileSync()
const firstFile = fs.readFileSync(process.argv[2], 'utf-8');
const secondFile = fs.readFileSync(process.argv[3], 'utf-8');
// The fs.readFileSync() is a synchronous function that reads the contents of a file synchronously,
// meaning that it blocks the execution of the program until the file is read..
// It takes two arguments: the file path and the encoding (optional).
// It returns the data read from the file directly as a string or a Buffer (depending on the encoding used).
// The utf-8 argument specifies the encoding of the file, which is set to 'utf-8' to read the file as text

// Concatenate the contents of the two files together
const concatenatedFile = firstFile + secondFile;

// Write the concatenated file to another file from the command line
fs.writeFileSync(process.argv[4], concatenatedFile, 'utf-8');

// Since this deals with command line arguments, we cannot print fileC to the console.
// console.log(printedFile);

/*
const firstFile = fs.readFile(process.argv[2]);
The fs.readFile() function read the contents of the first source file asynchronously.
The utf-8 argument specifies the encoding of the file, which is set to 'utf-8' to read the file as text
*/
