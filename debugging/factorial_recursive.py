#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Computes the factorial of a non-negative integer n using recursion.
        Factorial is defined as n! = n * (n-1) * ... * 1, and 0! = 1.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
