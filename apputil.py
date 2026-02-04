import seaborn as sns
import pandas as pd


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def to_binary(n):
    bin_string = ''
    for power in range(8, 0, -1):
        # Add a 1 if n is divisible by 2, else add 0
        if n // 2**power:
            bin_string += '1'

        else:
            bin_string += '0'

