#!/usr/bin/python3

# Written with ChatGPT

def fibonacci_iterative(n):
    # Initialize variables for the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Calculate and print Fibonacci sequence up to the given number
    while fib_sequence[-1] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print(fib_sequence[:-1])

fibonacci_iterative(10)

