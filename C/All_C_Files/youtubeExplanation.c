#include <stdio.h>
int Dan(int A, int N)
{
	return A*N;
}

int main()
{
	int c;
	int (*p)(int , int);
	p = &Dan;
	// p = Dan   -->> Using the function name will return the address of the function
	
	c = (*p)(2,5); //Deferencing and executing the function 'Dan'
	
	printf("Output is %d\n", c);
	
	return(0);
}
