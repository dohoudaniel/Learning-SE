//Creating a node in C - C Programming And Data Structures
//Youtube Video

//Creating the node of a singly linked list

//Mandatory library for standard input and output
#include <stdio.h>
//The library required to call the malloc function.
#include <stdlib.h>

/**
 *struct node- a node.
 * data - The data in the node, of any data type.
 * *link - A pointer to a nother node.
 */
struct node {
	int data;
	struct node *link
};

int main(void)
{
	struct node *head = NULL;
	// We use the malloc function to allocate memory for struct node, hereby creating the node with malloc.
	//We created a pointer and allocated memory for the node we created. We also stored the address of the node in the pointer.
	head = malloc(sizeof(struct node));
	head->data = 45; //With the help of the address, head can access the data inside the node. head has initialised data by 45, using this method.
	head->link = NULL; //Accessing the link part and initialising it with NULL.
	//printf("'data' is %d\n", head->data);	-> We used the head pointer to access data. The only way to access struct node is through the head pointer.
	
	//We created another node and another pointer, current, that points to the second node of the singly linkd list.
	//current points to and also stores the address of the second node.
	struct node *current = malloc(sizeof(struct node));
	current->data = 98;
	current->link = NULL;
	//Linking the first node to the second node.....
	head->link = current; //The link part of the first node now contains the address of the pointer current, whereby current hols the address of the second node.
	//Thus, the link part of the first node holds the address of the second node.
	
	
	//Creating the third node on the list
	struct node *myPtr = malloc(sizeof(struct node));
	myPtr->data = 100;
	myPtr->link = NULL;
	
	//Linking the second node to the third node
	current->link = myPtr;
	
	//We cannot continue using this method. This is unnecessary wastage of memory, as we will keep creating pointers for each node
	
	return (0);
}
