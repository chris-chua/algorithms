"""Stripe iterview question

Given an array of unsorted integers, find the 
first missing positive integer in linear time 
and constant space. The array can contain duplicates 
and negative numbers as well.
"""

# For each positive integer, swap it with the value 
# at # its index (which is 1 less than the integer).
# e.g. [3, 4, -1, 1] -> [1, -1, 3, 4]
# If the next value is not +1 of the previous value,
# then it's missing value.

def smallest_missing_positive_integer(arr):
    for idx, val in enumerate(arr):
        while val > 0 and val <= len(arr) and val - 1 != idx:
            arr[idx], arr[val - 1] = arr[val - 1] , val 
            idx = val - 1
            
    for i in range(len(arr)):
        if arr[i] >= 0 and arr[i] != i + 1:
            return i + 1
    return len(arr) + 1

if __name__ == '__main__':
    print(smallest_missing_positive_integer([3, 4, -1, 1])   ) 
    print(smallest_missing_positive_integer([1, 2, 0]))