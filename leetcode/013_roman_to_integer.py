class Solution:
    def romanToInt(self, s):
        """
        Args:
        s: str

        Output:
        int
        """
        lookup = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
                  
        total = lookup[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            value = lookup[s[i]]
            if lookup[s[i + 1]] > value:
                total -= value
            else:
                total += value
        return total

if __name__ == '__main__':
    print(Solution().romanToInt('XIV'))