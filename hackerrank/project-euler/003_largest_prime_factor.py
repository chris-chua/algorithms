# Project Euler Challenge 3
#!/usr/bin/env python3

def max_prime_factor(n):
    p = 2
    while (p*p <= n):
        if (n % p == 0):
            n //= p
        else:
            p +=2 if p>2 else 1 # after p = 2, consider only all odd numbers

    return n

t = int(input())
for _ in range(t):
    n = int(input())
    print(max_prime_factor(n))