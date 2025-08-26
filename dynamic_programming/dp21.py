"""
Longest Common Substring
"""
class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        maxi = 0
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        for ind2 in range(0, m+1):
            dp[0][ind2] = 0

        for ind1 in range(0, n+1):
            dp[ind1][0] = 0

        for ind1 in range(1, n+1):
            for ind2 in range(1, m+1):
                if text1[ind1-1] == text2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                    maxi = max(maxi, dp[ind1][ind2])
                else:
                    dp[ind1][ind2] = 0
        return maxi

text1 = "abcde"
text2 = "abce" 
s = Solution()
# print(s.longestCommonSubstring(text1, text2))

"""
Time complexity : O(n X m)
Space complexity : O(n X m)
dp
"""

"""
4. Tabulation [Space optimization]
"""
class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        maxi = 0
        prev = [0 for _ in range(m+1)]

        for ind1 in range(1, n+1):
            curr = [0 for _ in range(m+1)]
            for ind2 in range(1, m+1):
                if text1[ind1-1] == text2[ind2-1]:
                    curr[ind2] = 1 + prev[ind2-1]
                    maxi = max(maxi, curr[ind2])
                else:
                    curr[ind2] = 0
            prev = curr
        return maxi

text1 = "abcde"
text2 = "abgce" 
s = Solution()
print(s.longestCommonSubstring(text1, text2))

"""
Time complexity : O(n X m)
Space complexity : O(m)
"""