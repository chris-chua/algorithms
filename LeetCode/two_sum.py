from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        """
        Args:
        nums: List[int]
        target: int

        Output:
        List[int]
        """
        lookup = defaultdict()
        for idx, val in enumerate(nums):
            if (target - val) in lookup:
                return [lookup[target - val], idx]
            else:
                lookup[val] = idx
        return -1

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))