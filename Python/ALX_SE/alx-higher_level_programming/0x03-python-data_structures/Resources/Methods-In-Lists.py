""" Using methods in lists """
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# The count() method
print(fruits.count('apple'))
print(fruits.count('tangerine'))

# The index() method
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4

# The reverse() method
print(fruits.reverse())

# The append() method
fruits.append('grape')
print(fruits)

# The sort() method
fruits.sort()
print(fruits)

# The pop() method
fruits = ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())

# You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 1 This is a design principle for all mutable data structures in Python.
