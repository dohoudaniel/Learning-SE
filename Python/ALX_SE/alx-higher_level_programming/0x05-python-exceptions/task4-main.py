#!/usr/bin/python3
list_division = __import__('task4').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]

my_l_2 = [2, 0, "H", 2, 7]
# The try except block will come in here because the following are the exceptions:
# "H" - A wrong type, of type str
# 0 - There is a division by zero.

result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

