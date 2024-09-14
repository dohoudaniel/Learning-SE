#include <stdio.h>

int n = 10;
int *f = &n;

int main()
{
	printf("The value of f of n is %d\n", *f); //This prints the value of n using *f. This is what Dereferencing means
	printf("This is the address of n - %p\n", f); //This prints the address of n using 'f' or '&n'
	
	/*
	* *f = n = 10
	* f = &n = Address of n
	*/
	
	/* There are three ways to declare a pointer
	*int* myNum; // Most used
	*int *myNum;
	*int * myNum;
	*/
	return (0);
}
