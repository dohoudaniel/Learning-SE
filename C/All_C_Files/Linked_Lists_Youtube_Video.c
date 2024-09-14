//Singly Linked Lists Project
//Pair programming is extremely important

//This code is from the youtube video. Link --> https://youtu.be/udapt4FGY20
#include <stdlib.h>		//We include only stdlib.h here first before stdio.h is included
#include <stdio.h>

/**
 * @nodePtr: Pointer to a struct node
*/
/* A Linked list is 
*/
//We must have a pointer that points to the start of a linked list
//A node pointer is a pointer to a node
//A node is a struct that contains a node pointer
//struct defn and typedef below are
//broken into two parts for clarity and explaining
//in our code we would usually combine the two 
/**
We could define a list RECURSIVELY by saying that a List is either:
									Null
									Data folowed by a List (Data, List)
*/
//Recursive programs, and also non-recursive programs (^_^) are neat ways of dealing with linked lists

typedef struct node *nodePtr;

struct node {
	int data;
	nodePtr next;
}; 	// Note that ; is included after the } mark.

typedef struct node node;

int main(int argc, const char * argv[]) {
	nodePtr first = NULL;

	first = malloc(sizeof(node));		//A piece of memory
	first->next = NULL;
	
	//We could also have done it like this
	/*
	* node firstNode;
	* firstNode.next = *first;
	*/
	
	first->data = 61;
	
	//first->next = malloc(sizeof(node));
	//first->next->next = NULL;
	//first->next->data = 62;
	
	nodePtr temp;
	temp = malloc(sizeof(node));
	temp->next = first;
	first = temp;
	
	printf("Hello, World!\n");
	return (0);
}
