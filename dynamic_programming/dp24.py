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

    def minDistance(self, text1, text2):
        i = len(text1)
        j = len(text2)
        res = self.solve(i-1, j-1, text1, text2 )
        op1 = i - res
        op2 = j - res
        return op1 + op2
        # return i + j - (2 * res)
    

word1 = "pqrs"
word2 = "pmr"
s = Solution()
print(s.minDistance(word1, word2))