/**
 * Stack Implementation using a Linked List
 */

#include <stdio.h>

/* Create an empty stack */
node *create_stack()
{
	node* emptyStack;
	emptyStack = (node*)malloc(sizeof(node));
	emptyStack->next = NULL;
	return emptyStack;
}

void Push(int inputData, node *stack)
{
	node* newnode = (node*)malloc(sizeof(node));
	newnode->data = inputData;
	newnode->next = stack->next; // Should be first
	stack->next = newnode;
	// how about change the above 2 lines?
}

/* Pop an entry from the stack */
int Pop(node *stack)
{
	int temp;
	node* toBePopped;
	if (stack->next != NULL)
	{
		temp = stack->next->data;
		toBePopped = stack->next;
		stack->next = stack->next->next;
		free(toBepopped);
		return temp;
	}
	else {
		return 0; // Error code, you can define according to the demand
	}
}

/* Return the top element in the stack */
int top(node* stack)
{
	if (stack->next != NULL)
	{
		return stack->next->data;
	}
	else {
		return 0;
	}
}

// Determine if the stack is empty
int is_empty(node *stack)
{
	return (stack->next==NULL);
}
