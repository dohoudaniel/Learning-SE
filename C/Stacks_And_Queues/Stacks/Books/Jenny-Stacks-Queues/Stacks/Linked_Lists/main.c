/* main.c */
#include <stdio.h>
#include "stack.h"

/**
 * main - Entry point of the program
 *
 * Return: 0 on successful execution
 */
int main()
{
        // Create an empty stack
        node *myStack = create_stack();

        // Push elements onto the stack
        Push(1, myStack);
        Push(2, myStack);
        Push(3, myStack);

        // Pop elements from the stack and print them
        while (!is_empty(myStack))
        {
                printf("%d\n", Pop(myStack));
        }

        // Return 0 to indicate successful program execution
        return 0;
}

