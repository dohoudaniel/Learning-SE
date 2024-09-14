#include <stdio.h>
#include <string.h>

int main()
{
	int age = 16;
	/* 'address' is a pointer to age */
	int *address = &age;
	/* 'address' stores the address of 'age' as its value*/
	printf("The value of \'address\' is %u\n", *address); /* 16 */
	/* The pointer operator '*' is used to get the value of the variable that 'address' points to ('address' points to 'age', thus using
	 * '*address' in a printf statement prints the value of the variable 'age'.
	 * The pointer operator '*' is also known as a dereference operator.
	 */

	return (0);
}
