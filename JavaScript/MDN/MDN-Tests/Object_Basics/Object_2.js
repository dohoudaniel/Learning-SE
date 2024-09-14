/* Object 2 */
// Task 2
/*
Question
--------
In our next task, we want you to have a go at creating your own object literal to represent one of your favorite bands. The required properties are:

name: A string representing the band name.
nationality: A string representing the country the band comes from.
genre: What type of music the band plays.
members: A number representing the number of members the band has.
formed: A number representing the year the band formed.
split: A number representing the year the band split up, or false if they are still together.
albums: An array representing the albums released by the band. Each array item should be an object containing the following members:
name: A string representing the name of the album.
released: A number representing the year the album was released.
Include at least two albums in the albums array.

Once you've done this, you should then write a string to the variable bandInfo, which will contain a small biography detailing their name, nationality, years active, and style, and the title and release date of their first album.

Try updating the live code below to recreate the finished example:
*/

// Solution
let bandInfo;

// Put your code here
// I used the concept of constructors
const Daniel = {
  name: 'SpeedForce Codes',
  nationality: 'Nigeria',
  first_crush: 'Favour',
  genre: 'Jon Bellion Music',
  members: 1,
  formed: 2022,
  split: false,
  albums: {
    first: {
      name: 'A Beautiful Mind',
      released: 2022
    },
    middle: {
      name: 'The Human Condition',
      released: 2022
    },
    last: {
      name: 'Translation Through Speakers',
      released: 2022
    }
  }
};

// I will be using string concatenation
bandInfo = `Hello. This is ${Daniel.name}. I am based in ${Daniel.nationality}. `;
bandInfo = bandInfo + `'We' 😅 are not really a band, just ${Daniel.members}, person and `;
bandInfo = bandInfo + `I have loved Jon B.'s music since ${Daniel.formed}.\n`;
bandInfo = bandInfo + `I really love ${Daniel.genre} and I play it all the time. `;
bandInfo = bandInfo + `I found Jon Bellion's music through a girl I crushed on in ${Daniel.formed}. Her name is ${Daniel.first_crush}.\n`;
bandInfo = bandInfo + `Some of the albums I love the most are: ${Daniel.albums.first.name}, ${Daniel.albums.middle.name}, and ${Daniel.albums.last.name}.`;
console.log(bandInfo);

/*
// Don't edit the code below here
let para1 = document.createElement('p')
para1.textContent = bandInfo
section.appendChild(para1)
*/
