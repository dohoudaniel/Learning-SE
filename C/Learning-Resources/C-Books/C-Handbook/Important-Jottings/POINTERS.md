This file contains jottings on C Pointers:
- A pointer is the address of a block of memory that contains a variable.
- %p is the format specifier used for pointers in printf statements, while we use the ampersand too '&'. An example is: printf("The address of the variable 'age' is %p\n", &age); . We use the ampersand, '&', to get the value of the address in memory of a variable.
- Using int *address in the declaration, we are not declaring an integer variable, but rather a pointer to an integer.
- The pointer operator '*' is used to get the value of the variable an address is pointing to. '%u' is used with it in printf statements.
- 	int *address = &age;
        /* 'address' stores the address of 'age' as its value*/
        printf("The value of \'address\' is %u\n", *address); /* 16 */
	The pointer operator '*' is used to get the value of the variable that 'address' points to ('address' points to 'age', thus using '*address' in a printf statement prints the value of the variable 'age'. The pointer operator '*' is also known as a dereference operator.
