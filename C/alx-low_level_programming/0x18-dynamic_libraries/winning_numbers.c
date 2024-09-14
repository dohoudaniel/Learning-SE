/**
 * This is the code for the 2nd Advanced Tas
 * The Hint given was LD_PRELOAD
 * main - Generates set of winning numbers that match
 * the numbers chsen by the user.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int get_random_nums(int *numbers)
{
	/* Generate winning numbers that match the user's numbers. */
	numbers[0] = 9;
	numbers[1] = 8;
	numbers[2] = 10;
	numbers[3] = 24;
	numbers[4] = 75;
	numbers[5] = 9;

	/* Return success */
	return (0);
}
