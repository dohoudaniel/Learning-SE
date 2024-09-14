// Link: https://www.youtube.com/watch?v=xZuA5hA2yF8

// Name of file: Stack Creator App
// File used: stacks_using_arrays.c

#include <stdio.h>
#include <stdlib.h>

#define MAX 4

int stack_arr[MAX];
int stack_arr[MAX];

// top = -1 indicates that the stack is empty
int top = -1;

// This function checks if the stack if full or not.
// This function returns 0 if the stack is not full, and 1 if the stack is full.
// User can call this function to know if the stack is full or not.
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

// The isEmpty() function
// This function checks if the stack is empty or not.
//  can call this function to know if the stack is empty or not
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

// The push function
// The push function:
// 1. increments the 'top' variable by 1
// 2. Store the value at the index top
// We create the push function with 'void' because we do not want it to return anything.
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
}

//The pop() function.
//The pop() function deletes the last-entered element, and also returns the deleted element.
int pop()
{
	int value;


	// This code has been updated in the isEmpty() function

	// Code to ceck if the stack is empty
	if (top == -1)
	{
		printf("Stack underflow, i.e stack is empty.\n");
                exit(1); // We call the exit() function because we don't want to return an integer.
	}
	top = top - 1;
	value = stack_arr[top];
	return value;
}

//The peek() function.
//The peek() function deletes the last-entered element, and returns the top element of the stack.
int peek()
{
	int value;

	// Code to ceck if the stack is empty
	if (top == -1)
	{
		printf("Stack underflow.\n");
                exit(1); // We call the exit() function because we don't want to return an integer.
	}
	return stack_arr[top];
}

// A print function
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

int main()
{
	// Declare variables
	int choice, data;

	// Printing the requirements on the screen
	while(1)
	{
		printf("\n");
		printf("1. Push\n");
		printf("2. Pop\n");
		printf("3. Print the top element\n");
		printf("4. Print all the elements of the stack\n");
		printf("5. Quit\n");printf("Please enter your choice: ");
		scanf("%d", &choice);

		switch(choice)
		{
		        case 1:
		                printf("Enter the element to be pushed: ");
          		        scanf("%d", &data);
	 		        push(data);
		                break;

 	                case 2:
   		                data = pop();
	   		        printf("Deleted element is %d.\n", data);
	   		        break;

    		        case 3:
             		       	printf("The topmost element of the stack is %d.\n", peek());
		            	break;

     	    		case 4:
     			       	print();   // Calling the print function
		              	break;

               		case 5:
               		     	exit(1);   // Quiting the program if the user wants to quit.

               		default:
      				printf("Wrong choice.\n");
       		}
	}
	return (0);
}
