const promise1 = Promise.resolve('Success 1');
const promise2 = Promise.reject('Error 2');
const promise3 = new Promise((resolve, reject) => setTimeout(resolve, 1000, 'Success 3'));
const promise4 = new Promise((resolve, reject) => setTimeout(reject, 500, 'Error 4'));

//
Promise.allSettled([promise1, promise2, promise3, promise4])
  .then(results => {
    results.forEach((result, index) => {
      if (result.status === 'fulfilled') {
        console.log(`Promise ${index + 1} fulfilled with value: ${result.value}`);
      } else {
        console.log(`Promise ${index + 1} rejected with reason: ${result.reason}`);
      }
    });
  });
