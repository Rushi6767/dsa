"""
70. Climbing Stairs
"""
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)

n = 3
# print(climbStairs(n))

"""
Time complexity : O(2^n)
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""

def climbStairs(n, dp):
    if n <= 2:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = climbStairs(n-1, dp) + climbStairs(n-2, dp)
    return dp[n]

n = 3
dp = [-1] * (n+1)
# print(climbStairs(n, dp))

"""
Time complexity : O(n)
Space complexity : O(n) + O(n)
"""

"""
3. Tabulation [Bottom - Up]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
    
"""
Time complexity : O(n)
Space complexity : O(n)
"""

"""
4. tabulation (Space Optimation)
"""
n = 3
prev2 = 1
prev = 2

for i in range(2, n):
    curr = prev2 + prev
    prev2 = prev
    prev = curr

print(prev)

"""
Time complexity : O(n)
Space complexity : O(1)
"""