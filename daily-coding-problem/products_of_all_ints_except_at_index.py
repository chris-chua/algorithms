"""Uber interview question

Write a method get_products_of_all_ints_except_at_index() 
that takes an array of integers and returns an array 
of the products.

Example:
>>> get_products_of_all_ints_except_at_index([3, 2, 1])
[2, 3, 6]

>>> get_products_of_all_ints_except_at_index([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
[84, 12, 28, 21]
"""

# Analysis:
# A brute force approach would use two loops 
# to multiply the integer at every index by 
# the integer at every nestedIndex, unless 
# index == nestedIndex.
# This would give us a runtime of O(n^2).
# Instead, use a greedy approach in 2 passes, 
# (2 directions).
# https://www.interviewcake.com/question/python3/product-of-other-numbers
#
# Complexity:
# time O(n): 2 passses through input list
# space O(n): same length as input list

def get_products_of_all_ints_except_at_index(arr):
    if len(arr) < 2:
        raise IndexError('Requires at least 2 integers')

    # Create fixed length array to hold the products
    products_of_all_ints_except_at_index = [None] * len(int_list)
    
    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(arr)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= arr[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in range(len(arr) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= arr[i]

    return products_of_all_ints_except_at_index

if __name__ == '__main__':
    import doctest
    doctest.testmod()