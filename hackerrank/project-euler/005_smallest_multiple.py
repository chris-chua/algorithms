# Project Euler Challenge 5
#!/usr/bin/env python3

def gcd(x,y):
    '''
    int, int -> int
    This function implements the Euclidean algorithm to find the
    greatest common divisor of two numbers.
    '''

    while(y):
        x, y = y, x%y

    return x

def lcm(x, y):
    '''
    int, int -> int
    Returns the lowest common multiple of two numbers.
    '''

    lcm = (x * y)//gcd(x, y)
    return lcm

def multiple(n):
    '''
    int -> int
    Returns the lowest common multiple of each integer from 1 to n.
    '''
    if n==1:
        return 1
    else:
        m = 2
        i = 3
        while i <= n:
            m = lcm(m, i)
            i += 1
        return m

t = int(input())
for _ in range(t):
    n = int(input())
    print(multiple(n))