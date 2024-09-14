/* This is the C file used to understand token pasting in C */
/*
 * The token-pasting operator ## within a macro definition combines two arguments. It permits two
 * separate tokens in the macro definition to be joined into a single token.
 */
// stringize '#'

#include <stdio.h>

#define tokenpaster(n) printf ("token" #n " = %d\n", token##n)

int main(void)
{
	int token34 = 40;

	tokenpaster(34);
	return (0);
}

/* 
 * When the above code is compiled and executed, it produces the following result:
 * 	token34 = 40
 * How it happened, because this example results in the following actual output from the preprocessor:
 * 	printf ("token34 = %d", token34);
 * This example shows the concatenation of token##n into token34 and here we have used both stringize and token-pasting.
 */
