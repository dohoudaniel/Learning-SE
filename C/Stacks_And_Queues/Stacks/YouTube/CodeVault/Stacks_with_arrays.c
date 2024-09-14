/* Implementing a stack using an array*/
#include <stdio.h>
#include <string.h>
// #include <stdlib.h>

// Define an array of integers
int stack[256];
int count = 0;

// A push() operation
// It adds an integer passed in as an argument and adds it to the stack
void push(int x)
{
	if (count >= 256)
	{
		fprintf(stderr, "There's no space in the stack.\n'");
		// printf(stderr, "There's no space in the stack.\n'");
		return;
	}

	stack[count] = x;
	count++;
}

// The pop() method removes the last inserted element.
int pop()
{
	if (count == 0)
	{
		fprintf(stderr, "There's nothing to take from the stack.\n'");
		// exit(1);
		return -1;
	}
	int result = stack[count - 1];
	count--;
	return result;		// This is where the value of the pop() function is printed when called.
}

int main()
{
	printf("Stacks with arrays....\n");
	push(1);
	push(2);
	push(3);
	push(4);
	push(5);

	int i;
	for (i = 0; i < 5; i++)
	{
		printf("%d has been removed from the stack.\n", pop());
	}
	// return (0);
}
