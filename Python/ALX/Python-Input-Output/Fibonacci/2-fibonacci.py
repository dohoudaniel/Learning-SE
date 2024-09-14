#!/usr/bin/python3

# Written with ChatGPT

def fibonacci_recursive(n):
    # Recursive function to calculate Fibonacci number
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    # Calculate and print Fibonacci sequence up to the given number
    fib_sequence = []
    i = 0
    while fibonacci(i) <= n:
        fib_sequence.append(fibonacci(i))
        i += 1

    print(fib_sequence)


# Calling the function
fibonacci_recursive(10)

