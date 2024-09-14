#include <stdio.h>

int main()
{
	int i = 0;

	do {
		/* do something */
		printf("This is a do-while loop.\n");
		printf("The value of i is %i\n", i);
		i++;
	} while ( i < 10 );
/*
 * The block that contains the do something comment is always executed
 * at least once, regardless of the condition check at the bottom.
 * Then, until i is less than 10, we'll repeat the block.
*/
}
