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
    """ Finds the binary representation of an integer using recursion.

    Args:
        n (int): an integer to represent in binary

    Returns:
        str: the binary representation of n
    """

    # The base case will be when we have one digit of binary left
    if n < 2:
        return '1' if n == 1 else '0'

    # Otherwise, find the largest power of 2 that n contains
    max_power = int(np.log2(n))

    # Create a string representing that number in binary
    # (the padding with 0s will allow us to keep track of
    # 0 digits across the recursion. Otherwise, we would
    # only see 1s and never 0s)
    bin_string_a = '1' + '0' * (max_power)

    # Find the binary string for the smaller digits
    bin_string_b = to_binary(n - 2**max_power)

    # Replace the 0s in string a with string b, aligning them on the right
    a_len = len(bin_string_a)
    b_len = len(bin_string_b)
    return bin_string_a[0:a_len - b_len] + bin_string_b
