#include <stdio.h>
#include <string.h>

int main(void)
{
	int age = 16;
	/* Printing the address of the variable 'age'. */
	printf("The address of the variable 'age' is %p\n", &age);

	/* Assigning the address of one variable to another variable */
	/* creating a pointer of type int to an int variable */
	int *addressOfAge = &age;
	printf("The value of addressOfAge is %u\n", *addressOfAge);   /* Prints 16 */

	/* */
	int *address = &age;
	*address = 37;
	printf("The value of *address is %u\n", *address);   /* Prints 37 */


	/* Pointers in Arrays */
	/* Remember that the name of an array variable is actually a pointer to the first item of the array */
	/* This can be gotten using a printf statement. */
	/* Example: */
	int dan[10] = { 1, 3, 7, 10, 9, 6, 2, 8, 4, 5 };
	printf("The array \'dan\' points to %u, and %u is the first item of the array.\n", *dan, *dan);
	/* We can even print the other items in the array by using this principle */
	printf("I created an array \'dan\' and %u is the second item of the array \'dan\'.\n", *(dan + 1));
	printf("I created an array \'dan\' and %u is the third item of the array \'dan\'.\n", *(dan + 2));
	printf("I created an array \'dan\' and %u is the fourth item of the array \'dan\'.\n", *(dan + 3));

	return (0);
}
