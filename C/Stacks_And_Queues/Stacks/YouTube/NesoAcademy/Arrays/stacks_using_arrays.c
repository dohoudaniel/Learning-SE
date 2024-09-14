// Link: https://www.youtube.com/watch?v=Mlv2fMvt9b4

#include <stdio.h>
#include <stdlib.h>

#define MAX 4
int stack_arr[MAX];



// Declare our array globally
int stack_arr[MAX];

// The top variable stores the address of the most recent index in our stack
// top = -1 indicates that the stack is empty
// I think top stores the index number of the most recent variable in the array.
// Declare top globally
int top = -1;



/** This function checks if the stack if full or not.
This function returns 0 if the stack is not full, and 1 if the stack is full.
User can call this function to know if the stack is full or not.
*/
int isFull()
{
	if (top == MAX - 1)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}



/** The isEmpty() function
This function checks if the stack is empty or not.
User can call this function to know if the stack is empty or not
*/
int isEmpty()
{
	// Code to ceck if the stack is empty
	if (top == -1)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}


/* The push function */
/**
The push function:
1. increments the 'top' variable by 1
2. Store the value at the index top

We create the push function with 'void' because we do not want it to return anything.
*/



void push(int data)
{
	if (isFull())
	{
		printf("Stack Overflow, i.e stack is full.\n");
                return;
	}

	top = top + 1;		// The value of top is increased by 1 each time the function is called.
	stack_arr[top] = data;

	// Added a little modification here
	printf("%d has been added at index %d of the stack.\n", data, top);

	/*
	The code below has been updated in the isFull() function

	// Code to check if the stack is full.
	// It is important to check if the stack is full in the push function.
	if (top == MAX - 1)    // top = MAX - 1 = 4 - 1 = 3, and index 3 is the fourth element.
	{
		printf("Stack Overflow, i.e stack is full.\n");
                return;
	}
	// The if-statement comes before the other code and this is done so as to stop the function call
	// if top == MAX - 1. The stopping of the push function call is implemented using the empty
	// 'return' statement in the if-statement.
	*/

}



/**
The pop() function.
The pop() function deletes the last-entered element, and also returns the deleted element.
*/
int pop()
{
	int value;

	/*
	This code has been updated in the isEmpty() function

	// Code to ceck if the stack is empty
	if (top == -1)
	{
		printf("Stack underflow, i.e stack is empty.\n");
                exit(1); // We call the exit() function because we don't want to return an integer.
                // The exit(1) function call crashes the program, if the if-statement is met, i.e if the stack is empty.
                // exit(1) means abnormal termination of the program.
	}
	*/

	top = top - 1;
	value = stack_arr[top];
	return value;
}



/* A print function */
void print()
{
	int i; // A variable declared for the sake of the print() function's loop.
	if (top == -1)
	{
		printf("Stack underflow, i.e stack is empty.\n");
                return;
	}

	printf("\n"); // To print an empty line

	// A for-loop to print the values that have been popped.
	for (i = top; i >= 0; i--) // i is the same as top, and i was created for the sake of the loop in this function.
	{
		printf("%d at index %d of the stack has been popped.\n", stack_arr[i], i);
	}
}



/** The main() function */
int main()
{
	int data; // A variable declared for the sake of the pop() function

	push(1);
	push(2);
	push(3);
	push(4);
	push(5); // But wait. The stack is full!

	// data = pop(); // data is initialized because of pop()'s return value.
	// 4 is not printed to output because the pop() function is called.
	// 4 will only be printed when we do this
	// printf("%d\n", data);

	// Calling the print() function.
	print();
}
