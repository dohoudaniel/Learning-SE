/*
 * CPP - The C Pre-Processor
 */

#include <stdio.h>

/*
 * Lesson 1 - Conditionals
 * One of the things we can do is to use conditionals to change how our program will be compiled, depending on the value of an expression.
 */
#define BM 1

int main(void)
{
#if BM == 0
	printf("Be A Beautiful Mind 😎\n");
#else
	printf("A Beautiful Mind 👨‍💻🎧\n");
#endif
	//macro();
}


/* 
 * Lesson 2 - Symbolic Constants
 * We can define symbolic constants.
 */
#define VALUE 7
#define PI 3.142
#define NAME "Daniel"
/*
 * When we use NAME or PI or VALUE in our program, the preprocessor replaces its name with the value, before executing the program.
 * Symbolic constants are very useful because we can give names to values without creating variables at compilation time.
 */

/*
 * Lesson 3 - Macros
 * With #define we can also define a macro. The difference between a macro and a symbolic constant is that a macro can accept an argument and typically
 * contains code, while a symbolic constant is a value.
 */
#define POWER(x) ((x) * (x))
int macro()
{

	printf("%u\n", POWER(4)); 	//16
	// I called the function in the main function above
}


/*
 * Lasson 4 - if defined
 * We can check if a symbolic  constant or a macro is defined using #ifdef
 */
#define ABM 17
int ifdef()
{
#ifdef ABM
	printf("A Brautiful Mind is born!\n");
#elif
	printf("Be A Beautful Mind\n");
#endif
}
/*
 * We also have #ifndef to check for the opposite (macro not defined).
 * We can also use #if defined and #if !defined to do the same task.
 */
/*
 * It's common to wrap some block of code into a block like this:
 * 	#if 0
 * 	#endif
 * 
 * to temporarily prevent it to run, or to use a DEBUG symbolic constant:
 * 	#define DEBUG 0
 * 	#if DEBUG
 *  	//code only sent to the compiler
 *   	//if DEBUG is not 0
 * 	#endif
 */


/*
 * Lesson 5 - Predefined Symbolic Constants
 * The preprocessor also defines a number of symbolic constants you can use, identified by the 2 underscores before and after the name, including:
 * 	__LINE__ translates to the current line in the source code file
 * 	__FILE__ translates to the name of the file
 * 	__DATE__ translates to the compilation date, in the Mmm gg aaaa format
 * 	__TIME__ translates to the compilation time, in the hh:mm:ss format
 */
