"""Given an array of integers, return
indices of the two numbers such that
they add up to a specific target.

You may assume that each input would
have exactly one solution, and you
may not use the same element twice.

Example:
>>> print(get_indices_of_two_sum([2, 7, 11, 15], 9))
[0, 1]
"""

def get_indices_of_two_sum(arr, num):
    hashmap = {}
    for idx, val in enumerate(arr):
        if (num - val) in hashmap:
            return (hashmap[num - val], idx)
        else:
            hashmap[val] = idx
    return -1

print(get_indices_of_two_sum([2, 7, 11, 15], 9))