#!/usr/bin/python3

# Dealing with tuples and Python I/O
# Remember: Values of tuples cannot be modified or changed

myTuple = (1 , 2, 3, 5, 8)

# Printing the valus of tuples using indexes
print("1st Value:", myTuple[0])

# Prints from the first to the third, excluding the fourth
# Remember indexes!!!
print(myTuple[0:3])

# Print the length of the tuple
print("Tuple length:", len(myTuple))

# Creating another tuple
moreVals = myTuple + (13, 21, 34)

# Checking if an int is in a tuple
print("Is 34 in moreVals? :", 34 in moreVals) # Returns True

# Looping through the tuple and printing it
for i in moreVals:
    print(i)

# Converting a list into a tuple
aList = [55, 89, 144]
aTuple = tuple(aList)
print(isinstance(aTuple, tuple))

# Converting a tuple into a list
myList = list(aTuple)
print(isinstance(myList, list))

# Printing the minimum and maximum value inside a tuple.
print("Minimum value of 'aTuple' :", min(aTuple))
print("Maximum value of 'aTuple' :", max(aTuple))

