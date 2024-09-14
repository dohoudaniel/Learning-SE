#include <stdio.h>
#include <stdlib.>
#include <math.h>
#include <time.h>

/* Define a structure and declare a variable */
struct time
{
	int hh;
	int mm;
	int ss;
};
struct time t1;
t1.hh = 20;

/* Declare a pointer to struct time */
struct time *t1_ptr;

/* Store the address of a struct time variable in the pointer variable */
t1_ptr = &t1;

/* Access the member of the structure */
t1_ptr->hh = 21; // same as (*t1_ptr).hh = 21;
