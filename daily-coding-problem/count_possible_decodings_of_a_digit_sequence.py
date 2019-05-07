"""Facebook interview question

Given the mapping a = 1, b = 2, ... z = 26, 
and an encoded message, count the number of 
ways it can be decoded. You can assume that
the messages are decodable. For example, 
'001' is not allowed.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', 
and 'ak'.

Example:
>>> print(count_decodings(111))
3

>>> print(count_decodings(121))
3

>>> print(count_decodings(1234))
3
"""

# Analysis:
# time complexity = O(n)
# space complexity = O(n)
def count_decodings(digits):
    digits = str(digits)
    length = len(digits)

    # Create a fixed length string 
    # for memoization
    count = [0] * (length + 1)
    count[0] = 1
    count[1] = 1

    for i in range(2, length + 1):

        # If previous digit is not 0, then
        # previous digit must be added to
        # the count
        if digits[i - 1] > '0':
            count[i] = count [i - 1]

        # If second previous digit is 1 or 
        # 2 and last digit is smaller than
        # 7, then last two digits is a 
        # valid character
        if digits[i - 2] == '1' or (digits[i - 2] == '2' and digits[i - 1] < '7'):
            count[i] += count[i - 2]
        
    return count[length]

if __name__ == '__main__':
    import doctest
    doctest.testmod()