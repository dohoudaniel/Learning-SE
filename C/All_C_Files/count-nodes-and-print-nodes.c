//Traversing a Single Linked List (Counting the linked list)

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

//Program to count our number of nodes
void count_of_node(struct node *head) {
	int count = 0;
	if(head == NULL)
		printf("Linked List is empty!\n");
	struct node *ptr = NULL; 	//A pointer to a struct node
	ptr = head;
	while(ptr != NULL) {
		count++;
		ptr = ptr->link;
	}
	printf("The number of nodes in our linked list is %d\n", count);
}

//Program to print the data in our nodes
void print_data(struct node *head)
{
	if(head == NULL)
		printf("The linked list is empty!\n");
	struct node *ptr2 = NULL;
	ptr2 = head;
	while(ptr2 != NULL) {
		printf("The data in the linked lists are: %d\n", ptr2->data);
		ptr2 = ptr2->link;
	}
}

int main(void)
{
	//Creating the nodes
	
	struct node *head = malloc(sizeof(struct node));		//First node is created and let's assume it has an address of 1000
	head->data = 45;
	//head->link gives the address of the second node to be created
	head->link = NULL;		//head->link is null for now but head points to the first node with an address of 1000
	
	//current here points to the new second node and stores its address
	struct node *current = malloc(sizeof(struct node));		//Second node is created and let's assume it has a memory of 2000
	current->data = 98;
	current->link = NULL; //current->link is null for now but current points to the second node with an address of 2000
	//head->link = pointing to the second node of the list = current
	head->link = current; 	//Updated head->link from null to current. head->link now points to the address 200
	
	//current stops pointing to the second node and now points to the new third node and stores its adress
	current = malloc(sizeof(struct node));		//Third node is created and let's assume that it has an address of 3000
	current->data = 3;
	current->link = NULL; //Here, current->list is null for now, but current no longerpoints to the second node, it now points to the third node with an address of 3000
	//head->link->link points to the third node of the list = current
	head->link->link = current; //Updated head->link->link from null to current. head->link->link now points to the address 3000, which current here also was updated to point to.
	
	count_of_node(head);
	print_data(head);
	
	return (0);
}
