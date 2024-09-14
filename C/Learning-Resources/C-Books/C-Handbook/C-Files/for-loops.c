#include <stdio.h>
/* This c file explains for-loops */
int main()
{
	int dan;

	for (dan = 0; dan <= 10; dan++);
	{
	/*
	 * The initial condition: dan = 0.
	 * The test: dan <= 10
	 * The increment: dan++.
	 */
	// i is a common var name for loops.
	// j is a common name used for nested loops.
		printf("The value of \'dan\' is: %i\n", dan);
		// dan++;
		// TODO: Check the reason why the output for the value of dan is 11, when it is supposed to stop at 10.
	}

	printf("End of loop 😁\n");
}
