// Creating Queues with Arrays
// Link: https://www.youtube.com/watch?v=Ra6p-Bmajlw

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define an array globally
int queue[256];

int count;

// This function inserts into a queue
void insertIntoQueue(int x)
{
	// Checking if the queue is full
	if (count == 256)
	{
		printf("Queue is full. No more space.\n");
		exit(1); // I chose to end the program if the queue is full.
	}
	queue[count] = x;
	count++;
}

// This function removes from a queue
int removeFromQueue()
{
	// Checking if the queue is empty
	if (count == 0)
	{
		printf("Queue is already empty!\n");
 		exit(1);  // I chose to end the program if the queue is full.
	}

	int result = queue[0];
	int i;
	for (i = 0; i < count - 1; i++)
	{
		queue[i] = queue[i + 1];  // Updating the queue by moving all elements in it 1 index further.
	}
	count--;  // This will decrease because one item will be removed from the queue each time this function is called.
	return result;
}

int main(int *argc, char *argv[])
{
	insertIntoQueue(1);
	insertIntoQueue(2);
	insertIntoQueue(3);
	insertIntoQueue(4);

	int i;
	for (i = 0; i < count; i++)
	{
		printf("%d has been added to the queue.\n", queue[i]);
	}
	printf("\n"); // Printing a new line.

	int j;
	int localCount = count;
	for (j = 0; j < localCount; j++)
	{
		printf("%d has been removed from the queue.\n", removeFromQueue());
	}
	return (0);
}

