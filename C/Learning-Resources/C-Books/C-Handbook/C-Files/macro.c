// Practice file from lesson 20.3 - Macros 
#include <stdio.h>

#define POWER(x) ((x) * (x))
int macro()
{
	printf("%u\n", POWER(4));       //16
	// I called the function in the main function above
}

int main()
{
	macro();
	return (0);
}
