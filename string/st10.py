"""
13. Roman to Integer
"""

class Solution:
    def roman(self, s):
        n = len(s)
        number = 0
        roman = {"I":1,"V":5,"X" :10, "L" :50, "C" :100, "D" :500, "M" :1000}

        for i in range(n):
            if i<n-1 and roman[s[i]] < roman[s[i+1]]:
                number = number - roman[s[i]]
            else:
                number = number + roman[s[i]]
        return number

# s = "III"
s = "LVIII"
sol = Solution()
print(sol.roman(s))

"""
Time Complexity : O(n)
Space Complexity : O(7) == O(1)
"""