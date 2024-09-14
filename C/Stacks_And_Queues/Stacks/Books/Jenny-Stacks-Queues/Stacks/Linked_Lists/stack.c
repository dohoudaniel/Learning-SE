/* stack.c */

#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

/**
 * create_stack - Create an empty stack
 *
 * Return: Pointer to the newly created stack
 */
node *create_stack()
{
        // Allocate memory for a new stack
        node *emptyStack = (node *)malloc(sizeof(node));

        // Set the next pointer to NULL, indicating an empty stack
        emptyStack->next = NULL;

        // Return the pointer to the newly created stack
        return emptyStack;
}

/**
 * Push - Push an element onto the stack
 * @inputData: The data to be pushed onto the stack
 * @stack: Pointer to the stack
 */
void Push(int inputData, node *stack)
{
        // Allocate memory for a new node
        node *newnode = (node *)malloc(sizeof(node));

        // Set the data field of the new node
        newnode->data = inputData;

        // Adjust pointers to insert the new node at the top of the stack
        newnode->next = stack->next;
        stack->next = newnode;
}

/**
 * Pop - Pop an entry from the stack
 * @stack: Pointer to the stack
 * @temp: Stores the value of the popped element
 * @toBePopped: Stores the address of the top node.
 *
 * Return: The popped element or -1 if the stack is empty
 */
int Pop(node *stack)
{
        int temp;
        node *toBePopped;

        // Check if the stack is not empty
        if (stack->next != NULL)
        {
                // Store the data of the top node to be returned
                temp = stack->next->data;

                // Adjust pointers to remove the top node from the stack
                toBePopped = stack->next;
                stack->next = stack->next->next;

                // Free the memory occupied by the removed node
                free(toBePopped);

                // Return the popped element
                return temp;
        }
        else
        {
                // If the stack is empty, return -1 as an error code
                return -1;
        }
}

/**
 * top - Return the top element in the stack
 * @stack: Pointer to the stack
 *
 * Return: The top element of the stack or -1 if the stack is empty
 */
int top(node *stack)
{
        // Check if the stack is not empty
        if (stack->next != NULL)
        {
                // Return the data field of the top node
                return stack->next->data;
        }
        else
        {
                // If the stack is empty, return -1 as an error code
                return -1;
        }
}

/**
 * is_empty - Determine if the stack is empty
 * @stack: Pointer to the stack
 *
 * Return: 1 if the stack is empty, 0 otherwise
 */
int is_empty(node *stack)
{
        // Check if the stack is empty by examining the next pointer
        return (stack->next == NULL);
}
