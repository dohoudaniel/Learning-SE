1. This is the directory for the ALX SE C9 Simple Shell Project
2. When we run 'echo $$', it gives us the value of './ppid'
3. The maximum value an ID can have is 32768. Navigate to the home directory and navigate to proc/sys/kernel/ and cat pid_max
4. The command line arguments are passed through the main function: int main(int ac, char **av);
	av is a NULL terminated array of strings
	ac is the number of items in av
	av[0] usually contains the name used to invoke the current program. av[1] is the first argument of the program, av[2] the second, and so on.
5. 
