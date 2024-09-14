#include <stdio.h>
#include <string.h>

int main()
{
	// A string is an array of characters (a special kind of array)
	// E.g: char name[7];
	char name[15] =  { 'A', ' ', 'B', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l', 'M', 'i', 'n', 'd'};
	// A string literal is also known as a string constant.
	char Daniel[15] = "Beautiful Mind";
	// 'Beautiful Mind' is 14 chars long, but we define an array of 15 characters.
	// This is because the last character in a string MUST be a 0 value (the string terminator), and we must make space for it.
	
	// Use the format specifier '%s' in printf statements to print strings.
	printf("I am a %s \n", name);
	// Output: I am a A BeautifulMindBeautiful Mind

	return (0);
}
