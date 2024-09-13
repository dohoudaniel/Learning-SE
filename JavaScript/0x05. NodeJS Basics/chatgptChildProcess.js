// ChatGPT: https://chatgpt.com/share/13aef1e2-c763-45ce-bd96-feed1e320a6f
//
//
// Importing the child_process module
/* const { exec, spawn, fork } = require('child_process');
//
// Methods for creating child processes
// The exec method
exec('ls -l', (error, stdout, stderr) => {
  if (error) {
    console.error(`exec error: ${error}`);
    return;
  }
  console.log(`stdout: ${stdout}`);
  console.error(`stderr: ${stderr}`);
});
*/
//
// The spawn method
const { spawn } = require('child_process');
const ls = spawn('ls', ['-l']);
ls.stdout.on('data', (data) => {
  console.log(`stdout: ${data}`);
});
ls.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});
ls.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
