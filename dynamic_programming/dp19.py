"""
1143. Longest Common Subsequence
"""

def backtrac(index, subset, a, res):
    if index == len(a):
        res.append("".join(subset.copy()))
        return

    subset.append(a[index])
    backtrac(index + 1, subset, a, res)
    e = subset.pop()
    backtrac(index + 1, subset, a, res)


text1 = "abcde"
text2 = "ace" 
res1 = []
res2 = []
backtrac(0, [], text1, res1)
backtrac(0, [], text2, res2)
# print(res1)
# print(res2)

op = 0
l = -1

if len(res1) > len(res2):
    res = res1
    c = res2
res = res2
c = res1


for i in res:
    if i in c and len(i) != l:
        op+=1
        l = len(i)

# print(op)

"""
good try but above logic is not suitable
start by below
"""

class Solution:
    def solve(self, ind1, ind2, text1, text2):
        if ind1 < 0 or ind2 < 0:
            return 0
        
        if text1[ind1] == text2[ind2]:
            return 1 + self.solve(ind1-1, ind2-1, text1, text2)
        
        return max(self.solve(ind1-1, ind2, text1, text2), self.solve(ind1, ind2-1, text1, text2))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        return self.solve(m-1, n-1, text1, text2)



text1 = "abcde"
text2 = "ace" 
s = Solution()
# print(s.longestCommonSubsequence(text1, text2))

"""
Time complexity : O(2^n + 2^m)
Space complexity : O(n + m)  : stack space
"""

"""
2. Memoization [Top - Down]
"""

class Solution:
    def solve(self, ind1, ind2, text1, text2, dp):
        if ind1 < 0 or ind2 < 0:
            return 0
        
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
        
        if text1[ind1] == text2[ind2]:
            dp[ind1][ind2] = 1 + self.solve(ind1-1, ind2-1, text1, text2, dp)
            return dp[ind1][ind2]
        
        dp[ind1][ind2] = max(self.solve(ind1-1, ind2, text1, text2, dp), self.solve(ind1, ind2-1, text1, text2, dp))
        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(m-1, n-1, text1, text2, dp)



text1 = "abcde"
text2 = "ace" 
s = Solution()
# print(s.longestCommonSubsequence(text1, text2))

"""
Time complexity : O(2^n + 2^m)
Space complexity : O(n + m)  + O(n X m)
ss + dp
"""

"""
2. Memoization [Top - Down] with shifting concept
"""
class Solution:
    def solve(self, ind1, ind2, text1, text2, dp):
        if ind1 == 0 or ind2 == 0:
            return 0
        
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]
        
        if text1[ind1-1] == text2[ind2-1]:
            dp[ind1][ind2] = 1 + self.solve(ind1-1, ind2-1, text1, text2, dp)
            return dp[ind1][ind2]
        
        dp[ind1][ind2] = max(self.solve(ind1-1, ind2, text1, text2, dp), self.solve(ind1, ind2-1, text1, text2, dp))
        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return self.solve(m, n, text1, text2, dp)



text1 = "abcde"
text2 = "ace" 
s = Solution()
# print(s.longestCommonSubsequence(text1, text2))

"""
Time complexity : O(2^n + 2^m)
Space complexity : O(n + m)  + O(n X m)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        for ind2 in range(0, m+1):
            dp[0][ind2] = 0

        for ind1 in range(0, n+1):
            dp[ind1][0] = 0

        for ind1 in range(1, n+1):
            for ind2 in range(1, m+1):
                if text1[ind1-1] == text2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1])
        return dp[n][m]

text1 = "abcde"
text2 = "ace" 
s = Solution()
# print(s.longestCommonSubsequence(text1, text2))

"""
Time complexity : O(n X m)
Space complexity : O(n X m)
dp
"""

"""
4. Tabulation [Space optimization]
"""
# note: dont take -1, take 0

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        prev = [0 for _ in range(m+1)]
        for ind2 in range(0, m+1):
            prev[ind2] = 0

        for ind1 in range(1, n+1):
            curr = [0 for _ in range(m+1)]
            for ind2 in range(1, m+1):
                if text1[ind1-1] == text2[ind2-1]:
                    curr[ind2] = 1 + prev[ind2-1]
                else:
                    curr[ind2] = max(prev[ind2], curr[ind2-1])
            prev = curr
        return prev[m]

text1 = "abcde"
text2 = "ace" 
s = Solution()
print(s.longestCommonSubsequence(text1, text2))

"""
Time complexity : O(n X m)
Space complexity : O(m)
dp
"""