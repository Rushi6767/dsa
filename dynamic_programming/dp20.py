"""
Print Longest Common Subsequence
"""
class Solution:
    def printLongestCommonSubsequence(self, text1: str, text2: str) -> int:
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
        # print(dp)

        i, j = n, m
        result = []

        while i > 0 and j > 0:
            if text1[i -1] == text2[j-1]:
                result.append(text1[i-1])
                i -= 1
                j -= 1

            else:
                if dp[i][j-1] >= dp[i-1][j]:
                    j -= 1
                else:
                    i -= 1

        result.reverse()
        print("".join(result))

text1 = "abcde"
text2 = "bdgek" 
s = Solution()
s.printLongestCommonSubsequence(text1, text2)


"""
Time complexity : O(n X m  + (n + m)) 
Space complexity : O(n X m)

tc for reverse i am not considering
"""