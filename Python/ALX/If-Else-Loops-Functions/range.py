#!/usr/bin/python3

"""
The range() function
"""
for i in range(2, 10, 2):
    print(i)
print()

print(list(range(2, 20, 2)))
print("")

a = ['Mary', 'had', 'a', 'little', 'lamb']
# print(len(a))
for o in range(len(a)):
    print(o, a[o])
