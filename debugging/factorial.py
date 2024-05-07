#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print ("usage: python script.py <number>")
    sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)
