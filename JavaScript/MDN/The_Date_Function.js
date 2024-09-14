/**
 * This file has not been properly understood. Please revisit this,
 * and try more examples on it.
 */

/* The Date() function in JavaScript */
/* Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date */

// Several ways to create a Date object
/*
Note: When parsing date strings with the Date constructor (and Date.parse, they are equivalent),
always make sure that the input conforms to the ISO 8601 format (YYYY-MM-DDTHH:mm:ss.sssZ) — the parsing behavior
with other formats is implementation-defined and may not work across all browsers.
A library can help if many different formats are to be accommodated.
*/
const today = new Date();
const birthday1 = new Date('May 18, 2006 12:10:07'); // DISCOURAGED: May not work in all runtimes.
const birthday2 = new Date('2006-05-18T12:10:07'); // This is ISO8601-compliant and will work reliably
const birthday3 = new Date(2006, 5, 18); // the month is 0-indexed
const birthday4 = new Date(2006, 5, 18, 12, 10, 7); // The ISO 8601 format (YYYY-MM-DDTHH:mm:ss.sssZ)
const birthday5 = new Date(628021800000); // Passing epoch timestamp

// Formats of toString method returns values.
const date = new Date('2020-05-12T23:50:21.817Z');
date.toString(); // Tue May 12 2020 18:50:21 GMT-0500 (Central Daylight Time)
date.toDateString(); // Tue May 12 2020
date.toTimeString(); // 18:50:21 GMT-0500 (Central Daylight Time)
date.toISOString(); // 2020-05-12T23:50:21.817Z
date.toUTCString(); // Tue, 12 May 2020 23:50:21 GMT
date.toJSON(); // 2020-05-12T23:50:21.817Z
date.toLocaleString(); // 5/12/2020, 6:50:21 PM
date.toLocaleDateString(); // 5/12/2020
date.toLocaleTimeString(); // 6:50:21 PM

// To get Date, Month and Year or Time.
const myNewDate = new Date();
const [month, day, year] = [
  date.getMonth(),
  date.getDate(),
  date.getFullYear()
];
const [hour, minutes, seconds] = [
  date.getHours(),
  date.getMinutes(),
  date.getSeconds()
];

// Interpretation of two-digit years
let mySkilleddate = new Date(98, 1); // Sun Feb 01 1998 00:00:00 GMT+0000 (GMT)
mySkilleddate = new Date(22, 1); // Wed Feb 01 1922 00:00:00 GMT+0000 (GMT)
mySkilleddate = new Date("2/1/22"); // Tue Feb 01 2022 00:00:00 GMT+0000 (GMT)

// Legacy method; always interprets two-digit year values as relative to 1900
mySkilleddate.setYear(98);
mySkilleddate.toString(); // Sun Feb 01 1998 00:00:00 GMT+0000 (GMT)
mySkilleddate.setYear(22);
mySkilleddate.toString(); // Wed Feb 01 1922 00:00:00 GMT+0000 (GMT)

// Preferred method; never interprets any value as being a relative offset,
// but instead uses the year value as-is
date.setFullYear(98);
date.getFullYear(); // 98 (not 1998)
date.setFullYear(22);
date.getFullYear(); // 22 (not 1922, not 2022)

// Calculating elapsed time
// Using Date objects
const start = Date.now();

// The event to time goes here:
doSomethingForALongTime();
const end = Date.now();
const elapsed = end - start; // elapsed time in milliseconds

// Using built-in methods
const start2 = new Date();

// The event to time goes here:
doSomethingForALongTime();
const end2 = new Date();
const elapsed2 = end.getTime() - start.getTime(); // elapsed time in milliseconds
