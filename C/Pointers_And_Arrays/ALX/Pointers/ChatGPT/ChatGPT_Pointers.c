/* Code - ChatGPT's explanation on pointers */
#include <stdio.h>
#include <stdlib.h>

// Example 1
int pointer1()
{
	int age = 6; // Declare and initialize an integer
	int *agePointer = &age; // Declare a pointer to an integer
	// agePointer = &age; // Assign the memory address of the age variable to agePointer
	printf("My age is: %d\n", *agePointer);
	// Prints 'My age is: 6'.
	printf("\n");
}

// Example 2
int ponter2()
{
	int age = 16;
	int *agePtr;
	agePtr = &age;

	printf("The value of age is: %d\n", age); // Print the value of age.
	printf("The memory address of age is: %p\n", &age); // Print the memory address of age.
	printf("The value of agePtr is: %p\n"); // Print the value of agePtr (which is the memory address of age)
	printf("The value of the pointee of agePtr is: %d\n"); // Print the value of the pointee of 'agePtr' (which is the value of 'age')
}

int main()
{
	pointer1();
	pointer2();

	return (0);
}
