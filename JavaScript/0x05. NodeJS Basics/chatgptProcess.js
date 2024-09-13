// ChatGPT: https://chatgpt.com/share/13aef1e2-c763-45ce-bd96-feed1e320a6f
//
//
// Accessing and printing the 'process' object
// console.log(process);

// Process ID of the current process (pid)
console.log(`Process ID: ${process.pid}`);

// Process ID of the parent process (ppid)
console.log(`Parent Process ID: ${process.ppid}`);

// Process environment
// console.log(process.env);
console.log(`NODE_ENV: ${process.env.NODE_ENV}`);

// Process arguments (maybe the ones passed in into the command line)
console.log(`Process Arguments: ${process.argv}`);

// The current working directory of the NodeJS process
console.log(`Current directory: ${process.cwd()}`);

// Changing the current working directory
process.chdir('/path/to/new/directory');
console.log(`New directory: ${process.cwd()}`);

// Standard input, output and error streams
//
// Writing to standard output
process.stdout.write('Hello, World!\n');
//
// Writing to standard error
process.stderr.write('An error occurred!\n');
//
// Standard input
process.stdin.on('data', (data) => {
  console.log(`You entered: ${data.toString()}`);
});
//
//
// Exiting the process
/*
const someCondition = 'a condition';
if (someCondition) {
  console.log('Exiting with success');
  process.exit(0);
} else {
  console.error('Exiting with error');
  process.exit(1);
}
*/
//
// Handling signals
// Listening signals
process.on('SIGINT', () => {
  console.log('Received SIGINT. Exiting...');
  process.exit(0);
});
//
// Process events
// Listening for events
process.on('exit', (code) => {
  console.log(`Process exited with code: ${code}`);
});
process.on('uncaughtException', (err) => {
  console.error('There was an uncaught error:', err);
  process.exit(1); // Mandatory (as per the Node.js docs)
});
//
// Resource Usage Management
console.log(process.memoryUsage());
console.log(process.cpuUsage());
