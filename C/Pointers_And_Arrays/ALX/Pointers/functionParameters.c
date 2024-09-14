/**
 * modify_my_param - This function does not modify n
 * @m: A useless integer
 *
 * Return: Nothing.
 */
void modify_my_param(int m)
{
	m = 402;
}

/**
 * main - Parameters are passed by value
 *
 * Return: Always 0.
 */
int main(void)
{
	int n;

	n = 98;
	modify_my_param(n);

	return (0);
}
