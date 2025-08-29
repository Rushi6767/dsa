"""
1312. Minimum Insertion Steps to Make a String Palindrome
"""
class Solution:
    def solve(self, i, j, t1, t2):
        if i < 0 or j < 0:
            return 0
        
        if t1[i] == t2[j]:
            return 1 + self.solve(i-1, j-1, t1, t2)
        return max(self.solve(i-1, j, t1, t2), self.solve(i, j-1, t1, t2))

    def MInInsPalindrom(self, text1, text2):
        i = len(text1)
        j = len(text2)
        return self.solve(i-1, j-1, text1, text2 )

t1 = "aabc"
t2 = "aabd"
s = Solution()
print(s.MInInsPalindrom(t1, t2))

