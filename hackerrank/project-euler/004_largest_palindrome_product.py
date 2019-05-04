# Project Euler Challenge 4
#!/usr/bin/env python3

def is_palindrome(n):
    """
    Return True if and if a number is a palindrome.
    """

    n = str(n)
    return n == n[::-1]


def max_palindrome(n):
    """
    Return the maximum palindrome that is less than n,
    made from a product of 2 3-digit numbers .

    For a 6-digit palindrome, it must follow the form:
        100000a + 10000b + 1000c + 100c + 10b + a
        = 100001a + 10010b + 1100c
        = 11(9091a + 910b + 100c)

    Hence one of the factors must be a multiple of 11.

    Example:
    >>> max_palindrome(101110)
    101101
    >>> max_palindrome(800000)
    793397
    """

    pmax = 0

    # Search from 999 downwards
    for i in range(999, 100, -1):
        # If i is 999, then max j must be a multiple of 11, hence
        # j starts from 990. if i%11 is True, i.e. i is not a multiple
        # of 11, then j must be a multiple of 11.
        for j in range(990, 100, (-11 if i % 11 else -1)):
            p = i * j
            if p < pmax: break
            if p < n and is_palindrome(p): x, y, pmax = i, j, p

    return pmax if pmax > 0 else -1


t = int(input())
for _ in range(t):
    n = int(input())
    print(max_palindrome(n))