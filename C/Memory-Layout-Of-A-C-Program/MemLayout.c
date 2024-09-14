#include <stdio.h>

int myData; /* Uninitialized global variable stored in BSS */
int myData1 = 100; /* Initialized global variable stored in DS */

int main(void)
{
	int data; /* Local variable stored in stack */

	char *pStr = malloc(sizeof(char) * 4); /* Stored in the heap */

	static int mySecondData; /* Uninitialized static variable stored in BSS */
	static int mySecondData2 = 200; /* Initialized static variable stored in DS */

	return (0);
}
