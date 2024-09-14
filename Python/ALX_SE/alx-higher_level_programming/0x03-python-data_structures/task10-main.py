#!/usr/bin/python3
divisible_by_2 = __import__('task10').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0

# A while loop here looks like the combination of a for loop and an if loop
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1    # i increases by 1
    # the eqiuvalent of i = i + 1


"""
# My code
#!/usr/bin/python3
divisible_by_2 = __import__('task10').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0

# My pratical
for i in range(len(my_list)):
    if i != len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
# It works 
"""

