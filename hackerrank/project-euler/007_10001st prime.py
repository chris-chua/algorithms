# Project Euler Challenge 7
#!/usr/bin/env python3

def prime_sieve(n):
    """
    Return a list of prime numbers smaller than n using the sieve of Eratosthenes.

    Example:
    >>> prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> prime_sieve(11)
    [2, 3, 5, 7]
    """

    # Create an array to hold flags for all odd numbers greater or equal to 3.
    flags = [True] * (n // 2)

    # Loop from 3 to sqrt(n) for all odd numbers.
    for i in range(3, int(n ** 0.5) + 1, 2):
        # Check if flags[i] is a prime number.
        if flags[i // 2]:
            # Starting from i*i, set all multiples of i to False.
            flags[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [2 * i + 1 for i in range(1, n // 2) if flags[i]]


def n_prime(n):
    """
    Return the n-th prime number.

    Example:
    >>> n_prime(100)
    541
    >>> n_prime(10000)
    104729
    """

    import math
    # Calculates the upper-bound to perform prime_sieve.
    if n >= 6:
        upper = math.ceil(n * (math.log(n) + math.log(math.log(n))))
    else:
        # 5th prime is 11.
        upper = 12

    # Add a [0] placeholder so that primes[i] is the i-th element.
    primes = [0] + prime_sieve(upper)

    return primes[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(n_prime(n))