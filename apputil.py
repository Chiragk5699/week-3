import seaborn as sns
import pandas as pd
import numpy as np


def fibonacci(n):
    """ Finds the nth element in the Fibonacci sequence using recursion.

    Args:
        n (int): the index of the element

    Returns:
        int: the nth element in the sequence
    """

    # The base cases are the first two elements 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # The nth element is found by adding the previous two elements
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def to_binary(n):
    """ Finds the binary representation of an integer.

    Args:
        n (int): an integer to represent in binary

    Returns:
        str: the binary representation of n
    """

    # We will build the string one digit at a time
    bin_string = ''

    # Find the largest power of 2 (and therefore digit) of the number
    max_power = int(np.log2(n))

    # Check if n contains each power of 2 decreasing to 1
    for power in range(max_power, -1, -1):
        # If it contains that power, add a 1 to the string
        # and subtract the power from n
        if n >= 2**power:
            bin_string += '1'
            n -= 2**power

        # Otherwise, add 0 to the string
        else:
            bin_string += '0' 
    
    return bin_string

print(to_binary(2))
