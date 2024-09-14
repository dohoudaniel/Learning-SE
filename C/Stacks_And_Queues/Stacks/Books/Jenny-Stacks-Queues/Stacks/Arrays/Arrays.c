/* Implementing a stack using an array */

#include <stdio.h>
#include <stdlib.h>

typedef struct
{
        int *data;         // data is an array of integers
        int top;           // Position of the top element
        int size;          // Maximum number of data in the stack
} Stack;

/**
 * createStack - Create a stack with the given size
 * @aStack: Pointer to the stack structure
 * @size: Size of the stack
 *
 * Return: 1 for success, 0 for failure
 */
int createStack(Stack *aStack, int size)
{
        // Allocate memory for the stack array
        aStack->data = (int *)malloc(sizeof(int) * size);
        if (aStack->data == NULL)       // Malloc failed
        {
                return 0;
        }
        aStack->size = size;
        aStack->top = -1;               // Initialize top position to -1 (empty stack)
        return 1;
}

/**
 * makeEmpty - Make the stack empty by resetting the top position
 * @aStack: Pointer to the stack structure
 */
void makeEmpty(Stack *aStack)
{
        aStack->top = -1;               // Reset top position to -1 (empty stack)
}

/**
 * isEmpty - Check if the stack is empty
 * @aStack: Pointer to the stack structure
 *
 * Return: 1 if empty, 0 otherwise
 */
int isEmpty(Stack *aStack)
{
        if (aStack->top < 0)            // If top position is less than 0, stack is empty
        {
                return 1;
        }
        else {
                return 0;
        }
}

/**
 * isFull - Check if the stack is full
 * @aStack: Pointer to the stack structure
 *
 * Return: 1 if full, 0 otherwise
 */
int isFull(Stack *aStack)
{
        if (aStack->top >= aStack->size - 1)      // If top position is at the maximum capacity of the stack
        {
                return 1;
        }
        else {
                return 0;
        }
}

/**
 * top - Return the top element of the stack without removing it
 * @aStack: Pointer to the stack structure
 *
 * Return: Value of the top element, or 0 if empty (error code)
 */
int top(Stack *aStack)
{
        if (!isEmpty(aStack))           // If stack is not empty
        {
                return aStack->data[aStack->top];        // Return the value at the top position
        }
        else {
                return 0;               // Error code indicating empty stack
        }
}

/**
 * pop - Remove and return the top element of the stack
 * @aStack: Pointer to the stack structure
 *
 * Return: Value of the popped element, or 0 if empty (error code)
 */
int pop(Stack *aStack)
{
        if (!isEmpty(aStack))           // If stack is not empty
        {
                int aData = top(aStack); // Get the value of the top element
                aStack->top--;          // Decrement the top position to remove the element from the stack
                return aData;           // Return the popped element
        }
        else {
                return 0;               // Error code indicating empty stack
        }
}

/**
 * push - Push an element onto the top of the stack
 * @aStack: Pointer to the stack structure
 * @aData: Element to be pushed onto the stack
 *
 * Return: 1 for success, 0 for failure (if the stack is full)
 */
int push(Stack *aStack, int aData)
{
        if (!isFull(aStack))            // If stack is not full
        {
                aStack->top++;          // Increment the top position
                aStack->data[aStack->top] = aData;       // Assign the new element to the top position
                return 1;               // Success code indicating successful push
        }
        else {
                return 0;               // Failure code indicating full stack
        }
}
