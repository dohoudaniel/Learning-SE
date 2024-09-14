#!/usr/bin/node
// Importing the dict object from 101-data.js
const { dict } = require('./101-data.js');

// Create a new dictionary to store user ids by occurrence
const userIdsByOccurrence = {};

// Loop through the original dict object
for (const userId in dict) { //userId represents the keys in dict
  // console.log(userId);
  const occurrence = dict[userId];
  // console.log(occurrences);
  // console.log();

  // If the occurrence is not a key in the new dictionary, create an empty array as the value
  if (!userIdsByOccurrence[occurrence]) {
    userIdsByOccurrence[occurrence] = [];
  }

  // Push the userId into the array for the corresponding occurrence
  userIdsByOccurrence[occurrence].push(parseInt(userId));
}

// Print the new dictionary of user ids by occurrence
console.log(userIdsByOccurrence);
