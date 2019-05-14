"""Facebook interview question

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

# What we need to do:
# pick 1 random element from the stream
#
# How:
# create a random number generator
# return the max element which is a random element

"""
Args:
stream: List[any]

Output:
[any]
"""

from random import random

def pick_random_element(stream):
    max_value = 0
    value_idx = 0
    for i in range(len(stream)):
        random_value = random()
        if random_value > max_value:
            max_value = random_value
            value_idx = i
    return stream[value_idx]

if __name__ == '__main__':
    sample_stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(pick_random_element(sample_stream))