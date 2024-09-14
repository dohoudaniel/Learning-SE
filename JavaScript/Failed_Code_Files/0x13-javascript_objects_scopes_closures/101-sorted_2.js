#!/usr/bin/node
// This code did not pass the checker, and is therefore irrelevant

// Importing the dict object from 101-data.js
const { myJSDict } = require('./101-data').dict;

// Create a dictionary to store user ids by occurrence
const userIdsByOccurrence = {};

// Iterate through the dictionary of occurrences by user id
for (const userId in myJSDict) { // userId represents the keys in dict
  // console.log(userId);
  const occurrences = myJSDict[userId];
  // console.log(occurrences);
  // console.log();

  // Check if the number of occurrences is already a key in the new dictionary
  if (occurrences in userIdsByOccurrence) {
    // If so, push the user id to the list of user ids for that occurrence using the JS push() method
    userIdsByOccurrence[occurrences].push(parseInt(userId));
    // The push() method adds the specified elements to the end of an array and returns the new length of the array.
    // The parseInt function converts its first argument to a string, parses that string, then returns an integer or NaN.
  } else {
    // If not, create a new key in the new dictionary with the occurrence as the key
    // and an array containing the user id as the value
    userIdsByOccurrence[occurrences] = [parseInt(userId)];
  }
}

// Print the new dictionary of user ids by occurrence
console.log(userIdsByOccurrence);
