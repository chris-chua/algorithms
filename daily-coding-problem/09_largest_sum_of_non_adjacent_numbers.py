"""Airbnb interview question
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

>>> print(get_largest_sum_non_adjacent([2, 4, 6, 2, 5]))
13

>>> print(get_largest_sum_non_adjacent([5, 1, 1, 5]))
10

>>> print(get_largest_sum_non_adjacent([5, 5, 10, 40, 50, 35]))
80
"""

def get_largest_sum_non_adjacent(arr):
    incl = 0
    excl = 0

    for i in arr:
        # update max sum for two scenarios:
        # incl current and excl current
        incl, excl = excl + i, max(incl, excl)
    return max(incl, excl)

if __name__ == '__main__':
    import doctest
    doctest.testmod()       