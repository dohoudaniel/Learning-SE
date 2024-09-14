1. practice.c
	- practice.c:15:11: error: missing binary operator before token "printf"
	   15 | #if x > y printf("The product of x and y is %u\n", x * y)
	      |           ^~~~~~
	practice.c:16:14: error: missing binary operator before token "printf"
	   16 | #elif x == y printf("The value of x is %u\n", x)
	      |              ^~~~~~
	practice.c:17:13: error: missing binary operator before token "printf"
	   17 | #elif x < y printf("The difference between x and y is %u\n", y - x)
	      |             ^~~~~~
	practice.c:18:7: warning: extra tokens at end of #else directive [-Wendif-labels]
	   18 | #else printf("Breautiful Mind")
