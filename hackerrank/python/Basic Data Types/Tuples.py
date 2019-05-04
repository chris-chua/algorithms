""""
What is a hash object? 

Hash values are integers. 
They are used to quickly compare dictionary keys during a dictionary lookup. 
Numeric values that compare equal have the same hash value 
(even if they are of different types, as is the case for 1 and 1.0).

https://docs.python.org/3/library/functions.html#hash
""""

# read input and put them into a tuple: integer_tuple
_ = int(input())
integer_tuple = tuple(map(int, input().split()))

# print result
print(hash(integer_tuple))