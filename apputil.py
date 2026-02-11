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

    # If we get a negative n, we will return -1 to avoid infinite recursion
    if n < 0:
        return -1

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
    return bin_string_a[:a_len - b_len] + bin_string_b

# Get the data we need for the next functions
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    """ Returns a list of the column names sorted by the number of 
        missing items in ascending order.

    Returns:
        list: the list of column names
    """
    return list(df_bellevue.isna().sum().sort_values().index)


def task_2():
    """ Returns a dataframe showing the total admissions for each year.

    Returns:
        pandas.Dataframe: a dataframe with columns datetime(grouped by year) 
        and total_admissions
    """

    # First create a column for a datetime object so we can filter by year
    df_bellevue['datetime'] = pd.to_datetime(df_bellevue['date_in'])

    # Add another column for the total admissions for that year. We can count the last_name
    # because there are no missing elements
    df_bellevue['total_admissions'] = df_bellevue.groupby(df_bellevue['datetime'].dt.year)['last_name'].transform('count')
    return df_bellevue.groupby(df_bellevue['datetime'].dt.year)['total_admissions'].count().reset_index()


def task_3():
    """ Returns a series with the average age for each gender.

    Returns:
        pandas.Series: the average age indexed by gender
    """

    # I don't know what was meant by 'g' and 'h', so I will include them anyway
    # to preserve the original data as best as possible
    return df_bellevue.groupby('gender')['age'].mean().dropna()
    

def task_4():
    """ Returns a list of the 5 most common professions.

    Returns:
        list: the list of professions
    """

    # The value counts are already sorted by occurrences in descending order,
    # we just need the first 5
    return list(df_bellevue['profession'].value_counts()[0:5].index)


# A global dictionary to store the elements we have calculated
fibs = {0: 0, 1: 1}

def fibonacci_memorized(n):
    """ Finds the nth element in the Fibonacci sequence using data
    memorization to improve efficiency.

    Args:
        n (int): the index for the element in the Fibonacci sequence

    Returns:
        int: the nth element in the sequence
    """
    
    # If we get a negative n, we will return -1 to avoid infinite recursion
    if n < 0:
        return -1

    # Our new base case is when n can be found in the dictionary
    if n in fibs.keys():
        return fibs[n]

    # Now before returning the newly computed value, we need to update
    # the dictionary
    newValue = fibonacci_memorized(n - 1) + fibonacci_memorized(n - 2)
    fibs[n] = newValue
    return newValue
