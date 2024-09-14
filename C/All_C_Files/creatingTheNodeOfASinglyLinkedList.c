//Creating a node in C - C Programming And Data Structures
//Youtube Video

//Creating the node of a singly linked list

//Mandatory library for standard input and output
#include <stdio.h>
//The library required to call the malloc function
#include <stdlib.h>

/**
 *struct node- a node
 * data - The data in the node, NB: The data could be of any data type
 * *link - A pointer to a nother node
 */
struct node {
	int data;
	struct node *link
};

int main(void)
{
	struct node *head = NULL;
	// We use the malloc function to allocate memory for struct node, hereby creating the node with malloc.
	head = (struct node *)malloc(sizeof(struct node));		//We typecasted. The address of the struct node will be stored in the head pointer
	
	head->data = 45; //With the help of the address, head can access the data inside the node. head has initialised data by 45, using this method.
	head->link = NULL; //Accessing the link part and initialising it with NULL
	
	printf("'data' is %d\n", head->data);	//We used the head pointer to access data. The only way to access struct node is through the head pointer
	return (0);
}

//Output is 45
