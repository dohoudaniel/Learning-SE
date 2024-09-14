#!/usr/bin/python3

# fibonacci.py

import os

def fib(num):
    if num <= 1:
        return num
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

# Ask how many numbers they want:
numFibValues = int(input("How many Fibonacci values should be found: "))

# Loop while calling for each new number
i = 0
while i <+ numFibValues:
    # print("i = ", i)
    fibValue = fib(i)
    print(fibValue)
    i += 1
    
print("All done!")

