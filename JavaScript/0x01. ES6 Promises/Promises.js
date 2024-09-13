// Link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

// YouTube Video: https://www.youtube.com/watch?v=RvYYCGs45L4
/*
const ride = new Promise((resolve, reject) => {
  const arrived = true;
  if (arrived) {
    resolve('Driver arrived 🚗');
  } else {
    reject('Driver rejected your order 💔');
  }
});

ride
  .then(value => {
    console.log(value);
  })
  .catch(error => {
    console.log(error);
  })
  .finally(() => {
    console.log('Always A Beautiful Mind 🧘‍♂️');
  });
*/
//
// YouTube Video: https://www.youtube.com/watch?v=li7FzDHYZpc
// let question = 'A Beautiful Mind';
// let answer = 'Strings';
// console.log(`${question}: ${answer}`);

/**
const axiosRequest = require('axios');
axiosRequest
  .get('https://bored-api.appbrewery.com/random/') // https://httpstat.us/404/
  .then(response => {
    console.log(response.data.activity);
  })
  .catch(error => {
    console.error(`Error: ${error}`);
  });

// To test and prove that this is a Promise function,
// we would console log something, and it will run first
// JavaScript is asynchronous by default
console.log('Well, let\'s see if I\'ll be printed first.'); // Well, I was.
*/
const axiosRequest = require('axios');
async function getRequest() {
  try {
    const response = await axiosRequest.get('https://httpstat.us/500/'); // https://bored-api.appbrewery.com/random/
    console.log(response.data.activity);
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}
getRequest();
// To test and prove that this is a Promise function,
// we would console log something, and it will run first
// JavaScript is asynchronous by default
console.log('Well, let\'s see if I\'ll be printed first.'); // Well, I was.
