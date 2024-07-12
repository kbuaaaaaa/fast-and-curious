import math
from numba import jit

@jit(nopython=True)
def get_primes(n):
    '''
    Write primes under n to a specified file.
    :param n: int, The number to write primes under.
    :param path: str, The path to the file to write the primes to.
    :return: None
    '''
    # Delete the contents of the file if it already exists
    primes = []
    # Create a boolean array to mark numbers as prime or not
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Loop over all the possible prime numbers
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            # If the number is prime, mark all its multiples as non-prime
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Add the prime numbers to the list
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(str(i))
    return primes

def write_primes(n, path):
    # Write the list of primes to the file
    primes = get_primes(n)
    with open(path, 'w') as file:
        file.write('\n'.join(primes))


@jit(nopython=True)
def is_prime(n):
    '''
    Check if a number is prime.
    :param n: int, The number to check.
    :return: bool, True if the number is prime, False otherwise.
    '''

    # 0, 1, and negative numbers are not prime
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False

    # Consider odd numbers from 3 to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        # If a factor is found, the number is not prime
        if n % i == 0:
            return False
    # If no factors have been found, the number is prime
    return True