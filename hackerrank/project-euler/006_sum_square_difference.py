# Project Euler Challenge 6
#!/usr/bin/env python3

def ap_sum(n, d):
    '''
    Return the arithmetic progression sum of the multiples of d
    greater or equal to n.

    Example:
    >>> ap_sum(33, 3)
    198
    >>> ap_sum(33, 5)
    105
    '''
    # Find the number of terms in the arithmetic progression
    n //= d

    # Sum = d*m*(m+1)//2
    # where (m+1)//2 is the "average" value of each term

    return d * n * (n+1) // 2

t = int(input())
for _ in range(t):
    n = int(input())
    # We are asked to find the sum of multiples less than n
    print(ap_sum(n-1, 3) + ap_sum(n-1, 5) - ap_sum(n-1, 15))