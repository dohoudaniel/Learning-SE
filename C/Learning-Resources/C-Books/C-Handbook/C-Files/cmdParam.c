/* Command Line Parameters */

#include <stdio.h>

int main(int argc, char *argv[])
{
	/*
	 *  argc is an inreger number that contains the number of parameters provided in the command line.
	 *  argv[] is an array of strings.
	 *  Note that there's always at least one item in the argv array: the name of the program
	 */
	for (int i = 0; i < argc; i++)
	{
		printf("The command entered from the command line is %s\n", argv[i]);
	}
	return (0);
}
