#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.
    
    Parameters:
    n (int): The number for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of the number 'n'.
    """
    if n == 0:
        return 1  # The factorial of 0 is 1 by definition
    else:
        return n * factorial(n-1)  # Recursive step: multiply 'n' by the factorial of 'n-1'

# Get the number from command line arguments, calculate its factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)

