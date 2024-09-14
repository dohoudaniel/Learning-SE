# The range() function
- The range() function in Python is used to generate a sequence of numbers that can be iterated over using a loop. It takes one, two or three arguments, depending on how you want to generate the sequence. 
- Here are the different ways to use the range() function in Python:
1. With one argument:
If you provide one argument to the range() function, it generates a sequence of numbers starting from 0 up to, but not including, the provided argument. For example:
	# Generate a sequence of numbers from 0 to 4```
	for i in range(5):
    		print(i)
	
	Output:
	0
	1
	2
	3

2. With two arguments:
If you provide two arguments to the range() function, it generates a sequence of numbers starting from the first argument up to, but not including, the second argument. For example:
	# Generate a sequence of numbers from 2 to 6
	for i in range(2, 7):
		print(i)

	Output:
	2
	3
	4
	5
	6

3. With three arguments:
If you provide three arguments to the range() function, it generates a sequence of numbers starting from the first argument up to, but not including, the second argument, with a step size of the third argument. For example:
	# Generate a sequence of even numbers from 0 to 10
	for i in range(0, 11, 2):
    		print(i)

	Output:
	0
	2
	4
	6
	8
	10
- You can use the range() function in many ways depending on your requirements. It is commonly used in for loops to iterate over a sequence of numbers.
