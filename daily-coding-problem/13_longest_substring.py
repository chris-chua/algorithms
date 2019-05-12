"""Amazon interview question

Given an integer k and a string s, find the 
length of the longest substring that contains 
at most k distinct characters.

For example, given s = "abcba" and k = 2, the
longest substring with k distinct characters 
is "bcb".

https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_11_15.py
"""

def longest_substring(string, k):
    """
    
    Args:
        string(string)
        k(int)
    Returns:
        int: count of the length of the longest substring
    """

    assert(len(string) >= k)

    start_index = 0
    end_index = k
    max_length = k

    while end_index < len(string):
        end_index += 1
        while True:
            distinct_chars = len(set(string[start_index:end_index]))
            if distinct_chars <= k:
                break
            start_index += 1
        max_length = max(max_length, end_index - start_index)
    return max_length

if __name__ == '__main__':
    s = 'abcba'
    k = 2
    print(longest_substring(s, k))