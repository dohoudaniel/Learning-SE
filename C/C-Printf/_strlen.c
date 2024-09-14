#include "main.h"

/**
 * _strlen - Gets the length of a string
 *
 * @str: string of chars
 *
 * Return: Length of string
 * or -1 if someting went wrong
 */
int _strlen(char *str)
{
	int len = 0;

	if (str == NULL)
		return (-1);

	while (*str != '\0')
	{
		len++;
		str++;
	}

	return (len);
}

/**
 * main - Entry point of the program
 *
 * Return: Always 0
 */
int main(void)
{
	char *str = "Hello there, Dohou Daniel. Keep riding the lightning, and never give up.";
	int len = 0;

	len = _strlen(str);

	printf("The length of this string is: %d\n", len);

	return (0);
}
