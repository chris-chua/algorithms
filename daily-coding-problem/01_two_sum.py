"""Google interview question

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def can_two_sum(arr, target):
    num_seen_set = set()
    for num in arr:
        if target - num in num_seen_set:
            return True
        else:
            num_seen_set.add(num)
    return False

if __name__ == '__main__':
    test_list = [10, 15, 3, 7]
    k = 17
    print(can_two_sum(test_list, k))