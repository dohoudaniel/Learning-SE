#include <stdio.h>

int myGlobalVar; /* Stored in uninitialized area (BSS) */
int myGlobalVar2 = 10; /* Stored in initialized area (DS) */

int main(void)
{
	static int data; /* Stored in uninitialized area (BSS) */
	static int data2 = 10; /* Stored in initialized area (DS) */
	return (0);
}
