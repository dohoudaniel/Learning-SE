/**
 * Link: https://everythingcomputerscience.com/discrete_mathematics/Stacks_and_Queues.html#:~:text=Stack%20is%20a%20container%20of,%2Dout%20(FIFO)%20principle.
 */

// Arup Guha
// 6/20/07
// Written in COP 3502 to illustrate an array implementation of a stack.

#include <stdio.h>

// The array will store the items in the stack, first in
// index 0, then 1, etc. top will represent the index
// to the top element in the stack. If the stack is
// empty top will be -1.

#define SIZE 10
#define EMPTY -1

struct stack {
	int items[SIZE];
	int top;
};

void initialize(struct stack* stackPtr);
int full(struct stack* stackPtr);
int push(struct stack* stackPtr, int value);
int empty(struct stack* stackPtr);
int pop(struct stack* stackPtr);
int top(struct stack* stackPtr);

/**
 * main - The mian function for this stack program.
 */
int main(void)
{
	int i;
	struct stack mine;

	// Set up the stack and push a couple items, then pop one.
	initialize(&mine);
	push(&mine, 4);
	push(&mine, 5);
	printf("Popping %d\n", pop(&mine));

	// Push a couple more and test top.
	push(&mine, 22);
	push(&mine, 16);
	printf("At top now = %d\n", top(&mine));

	// Pop all three off.
	printf("Popping %d\n", pop(&mine));
	printf("Popping %d\n", pop(&mine));
	printf("Popping %d\n", pop(&mine));

	// Checking the empty function.
	if (empty(&mine))
	{
		printf("The stack is empty as expected.\n");
	}

	// Fill the stack.
	for (i = 0; i<10; i++)
	{
		push(&mine, i);
	}

	// Check if full works
	if (full(&mine))
	{
		printf("This stack is full as expected.\n");
	}

	// Pop everything back off.
	for (i = 0; i<10; i++)
	{
		printf("popping %d\n",pop(&mine));
	}

	system("PAUSE");

	return (0);
}

// If the push occurs, 1 is returned. 
// If the stack is full and the push can't be done, 0 is returned.

