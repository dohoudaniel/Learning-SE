# Steps taken in this experiment:
1. Write an empty C program:
	#include <stdio.h>
	
	int main(void)
	{
		return (0);
	}
2. Declare the following as follows sequentially below, but immediately fter the declaration of the variable, compile the file, and check the size of the compiled file using 'size':
- a static uninitialized variable ( Example: static int data; )
- an initialized static variable ( Example: static int data = 10; )
- a global uninitialized variable ( It is added outside any function. Example: int data; )
- an initialized global variable ( It is added outside any function. Example: int data = 10; )


# Note:
When an empty C program is created:
- Add a global uninitialized variable, compile the c file, and check the size.
- Then vi into the c file, and now,  add a static uninitialized variable, compile the c file, and check the size.
	- You would notice that the size of .bss increases as per the uninitialized global and static variables.
- Now add an initialized globalvariable and an initialized static variable, compile the c file, and check the size.
	- You would notice that the size of the data segment increases as per the initialized global and static variables.
