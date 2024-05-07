#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <number>")
        sys.exit(1)  # Exit the script if no argument is provided

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Please enter a non-negative integer.")
            sys.exit(1)
        f = factorial(num)
        print(f)
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

