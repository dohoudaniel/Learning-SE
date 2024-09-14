#include <stdio.h>

/* You can also define constants like this: */
#define AGE 37

int main()
{
	/* The value of age is constant, and does not change */
	const int age = 37;

	printf("The value of age is: %i, and the value of AGE is: %i\n", age, AGE);
	
	return (0);
}
