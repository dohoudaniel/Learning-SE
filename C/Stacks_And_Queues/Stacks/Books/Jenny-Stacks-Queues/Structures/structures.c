#include <stdio.h>
#include <stdlib.h>

struct time
{
	int hh;
	int mm;
	int ss;
};
...
struct time t1;
t1.hh = 20;
t1.mm = 12;
t1.ss = 30;
printf(“The time is %d:%d:%d”, t1.hh, t1.mm, t1.ss);
