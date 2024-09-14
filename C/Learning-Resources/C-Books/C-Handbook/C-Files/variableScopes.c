/* This file explains variable scopes in C. It also contains important jottings too. */
#include <stdio.h>
#include <stdlib.h>

int dan = 20; //A variable defined outside of a function is a global variable.
/* 
 * Global variables are accessible from any function of the program, and they
 * are available for the whole execution of the program, until it ends.
 */

int main()
{
	int age = 16; // 'age' is a local variable
	/* 
	 * Local variables are only accessible from within the function, and when the
	 * function ends they stop their existence. They are cleared from the memory
	 * (with some exceptions).
	 *
	 * The reason is that local variables are declared on the stack, by default,
	 * unless you explicitly allocate them on the heap using pointers, but then you
	 * have to manage the memory yourself.
	 */
}
