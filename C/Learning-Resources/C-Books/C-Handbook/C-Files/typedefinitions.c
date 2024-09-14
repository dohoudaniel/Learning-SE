/* This C Program contains an easy definition of a typedef and my code of trying to see how it works */
#include <stdio.h>
#include <stdlib.h>

int main()
{
	typedef int INT;
	INT dan = 10;
	
	printf("dan is of type int and holds the value %u\n", dan);
	return (0);
}
