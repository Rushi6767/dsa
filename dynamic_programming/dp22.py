"""
516. Longest Palindromic Subsequence
"""

class Solution:
    def solve(self, ind1, ind2, text1, text2):
        if ind1 < 0 or ind2 < 0:
            return 0
        
        if text1[ind1] == text2[ind2]:
            return 1 + self.solve(ind1-1, ind2-1, text1, text2)
        
        return max(self.solve(ind1-1, ind2, text1, text2), self.solve(ind1, ind2-1, text1, text2))

    def longestCommonSubsequence(self, s: str) -> int:
        text1 = s
        text2 = text1[::-1]
        m = len(text1)
        n = len(text2)
        return self.solve(m-1, n-1, text1, text2)


s = "bbbab"
s1 = Solution()
print(s1.longestCommonSubsequence(s))