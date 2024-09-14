/* Enumerated Types in C */
#include <stdio.h>

/* Using the typedef and enum keywords we can define a type that can have
 * either one value or another.
 * It's one of the most important uses of the typedef keyword.
 */
/* An idea of an example of an enumerated type:
 * typedef enum {
 * 	true,
 * 	false
 * 	} BOOLEAN;
 */

typedef enum {
	January,
	February,
	March,
	April,
	May,
	June,
	July,
	August,
	September,
	October,
	November,
	December
} MONTHS;

int main(void)
{
	MONTHS month = May;

	if (month == May) {
		printf("We already are in the fifth month of the year. How time files👨‍💻🎧");
	} else {
		printf("Criticization");
	}
}

/*
 * Every item in the enum definition is paired to an integer, internally. So in
 * this exampleJanuary is 0, February is 1 and so on.
 */
