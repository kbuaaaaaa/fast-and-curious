from numba import njit

@njit
def fibonacci(n, memo=None):
    """
    Calculate the nth Fibonacci number using dynamic programming.

    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, usually starting with 0 and 1. This function 
    uses dynamic programming with memoization to calculate the Fibonacci number at position n.

    Parameters:
    n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.
    memo (dict): A dictionary to store the previously calculated Fibonacci numbers.

    Returns:
    int: The nth Fibonacci number.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(9)
    34
    """
    if memo is None:
        memo = [0, 1]
    
    if n < len(memo):
        return memo[n]
    
    while len(memo) <= n:
        memo.append(memo[-2] + memo[-1])
    
    return memo[n]