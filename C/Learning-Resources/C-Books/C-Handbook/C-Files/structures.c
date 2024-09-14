/*
 * Using the struct keyword we can create complex data structures using
 * basic C types.
 * A structure is a collection of values of different types. Arrays in C are limited
 * to a type, so structures can prove to be very interesting in a lot of use cases.
 * 
 * Structures are used in linkd lists.
 */
#include <stdio.h>

int Daniel()
{
	struct bm {
		int age;
		char *name;
	} height; //You can declare variables that have as type that structure by adding them after the closing curly bracket, before the semicolon.

	struct bm details = { 16, "Beautiful Mind"}; //Structures can be defined like this
	// Printing details from a struct
	printf("I am Dohou Daniel. I am %u years old. I am a male, and I am known as A %s.\n", details.age, details.name);
	
	// We can also change the values of a structusing the dot notation, like in the printf statement.
	details.age = 17;
	printf("I am turning %u this year (2023).\n", details.age);

	return (0);
}

/*
 * Structures are very useful because we can pass them around as function
 * parameters, or return values, embedding various variables within them, and
 * each variable has a label.
 * It's important to note that structures are passed by copy, unless of course
 * you pass a pointer to a struct, in which case it's passed by reference.
 */

int Dohou()
{
	typedef struct {
		int age;
		char *name;
	} TIME;
	// The structure we create using typedef is usually, by convention, uppercase.
	// Now we can declare new TIME variables like this:
	TIME time;
	TIME reality = { 17, "To the Future"};

	printf("I now understand how \'typedef\' and \'struct\' are used in singly linked lists, and why they are used too.\n");
}

int main()
{
	Daniel();
	Dohou();

	return (0);
}
