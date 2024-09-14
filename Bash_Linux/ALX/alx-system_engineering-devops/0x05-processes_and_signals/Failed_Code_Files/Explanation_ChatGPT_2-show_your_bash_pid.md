Certainly! Here's an example of a Bash script that displays lines containing the word "bash" and extracts the PID of the Bash process:

```bash
#!/bin/bash
# shellcheck disable=SC2009

ps auxf | grep bash | grep -v grep | awk '{print $2}'
```

In this script, we use a combination of commands to achieve the desired result:

- `ps auxf` is used to list all processes in a user-oriented format, including the Bash processes.
- `grep bash` filters the lines that contain the word "bash" from the output of the previous command.
- `grep -v grep` excludes the line containing the actual `grep` command itself from the result.
- `awk '{print $2}'` extracts and prints the second column, which contains the PID.

By running this script, you'll get the PID(s) of the Bash process(es) running on your system. Remember to give the script execute permissions (`chmod +x scriptname.sh`) before running it.

Note: The `# shellcheck disable=SC2009` comment is used to disable the specific shellcheck warning SC2009, which flags the use of `grep` with a process substitution. In this case, it is safe to ignore the warning because we are using it as intended.
