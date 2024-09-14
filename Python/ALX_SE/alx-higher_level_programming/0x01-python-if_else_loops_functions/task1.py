#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)    # specifies the range for which the random numbers are chosen.
if number >= 0:
    last_num = number % 10    # last_num here will store the last number of number (the remainder)
elif number < 0:
    last_num = (abs(number) % 10 * -1)
    # last_num contains the negative value of the absolute value of remainder of number
    # The abs() function returns the absolute value of the specified number

print('Last digit of {0} is {1}'.format(number, last_num), end=" ")

if last_num > 5:
    print("and is greater than 5")
elif last_num == 0:
    print('and is 0')
elif last_num < 6 and last_num != 0:
    print('and is less than 6 and not 0')

