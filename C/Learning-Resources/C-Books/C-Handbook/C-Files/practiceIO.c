/* Praticing how input and output work with strings */
/* The file takes in only 20 characters */

#include <stdio.h>
int main(void)
{
	char name[20];
	printf("Enter your name: ");
	scanf("%s", name);
	printf("Your name is %s\n", name);
	return (0);
}
