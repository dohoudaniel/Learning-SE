/* Working with global variables in C */
#include <stdio.h>

int belEsprit = 1;

int daniel()
{
	belEsprit = belEsprit + 9;
	printf("belEsprit is %u\n", belEsprit);
	return (0);
}

int main()
{
	daniel();

	return (0);
}
