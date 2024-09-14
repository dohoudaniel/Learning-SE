#include <stdio.h>

int main()
{
	// Every value in an array, must have the same type.
	// An array can be defined like this.
	int beautiful[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	/* The size of the array must be specified */
	// You can use a constant to define the size of an array.
	// const int SIZE = 10;
	// int minds[SIZE];
	// Initialization of an array:
	// int array[SIZE] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	// You can also assign a value after the definition of the array:
	// minds[0] = 0; 	// Initialization of arrays start from the base 'slot', 0
	// minds[1] = 1;

	// You can use a loop for arrays.
	int prices[5];
	int i;
	for (i = 0; i < 5; i++)
	{
		prices[i] = i + 1;
	}

	// You reference arrays using their index values
	printf("The value of beautiful[8] is %i\n", beautiful[8]);
	printf("The value of beautiful[7] is %i\n", beautiful[7]);

	// Finding the length of an array
	int lengthOfTheArray;  // Size of whole array in memory
	int lengthOfArray;	    // Number of elements in the array
	lengthOfTheArray = sizeof(beautiful);
	lengthOfArray = sizeof(beautiful) / sizeof(int);
	printf("The length of beautiful[10] in memory is %i\n", lengthOfTheArray); // Prints the number of elements in the array (10) * size of an int (4) = 40
	printf("The number of elements in beautiful[10] is %i\n", lengthOfArray); // Prints the number of elements in the array = 10

	return (0);

	// Arrays indexes start from 0, so an array of 5 items, like the prices array above, will have items ranging from 0 to 4.
	// Elements in an array are stored sequentially, one right after the other.
	// The variable name of an array (e.g 'prices' like above) is a pointer to the first element of the array, and can also be used as a normal pointer.
}
