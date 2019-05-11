"""Amazon interview question
There exists a staircase with N steps, and you can climb 
up either 1 or 2 steps at a time. Given N, write a function 
that returns the number of unique ways you can climb the 
staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a 
time, you could climb any number from a set of positive 
integers X? For example, if X = {1, 3, 5}, you could climb
 1, 3, or 5 steps at a time.
"""

def count_unique_ways(N, steps={1, 2}):
    cache = [0] * (N + 1)
    cache[0] = 1
    cache[1] = 1
    for i in range(2, N + 1):
        for k in steps:
            if k <= i:
                cache[i] += cache[i - k]
    return cache[-1]

if __name__ == '__main__':  
    print(count_unique_ways(4))
    print(count_unique_ways(10, {1, 3, 5}))