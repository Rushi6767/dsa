"""
Frog jump
"""
def frog(index):
    if index == 0:
        return 0
    jump1 = frog(index - 1) + abs(heights[index] - heights[index -1])

    if index > 1:
        jump2 = frog(index - 2) + abs(heights[index] - heights[index -2])
    else:
        jump2 = float("inf")

    return min(jump1, jump2)


heights = [20, 30, 40, 20]
n = len(heights) - 1
# print(frog(n))

"""
Time complexity : O(2^n)
Space complexity : O(n)
"""

"""
memoization
"""
def frog(index, dp):
    if index == 0:
        return 0
    
    if dp[index] != -1 :
        return dp[index]
    jump1 = frog(index - 1, dp) + abs(heights[index] - heights[index -1])

    if index > 1:
        jump2 = frog(index - 2, dp) + abs(heights[index] - heights[index -2])
    else:
        jump2 = float("inf")

    dp[index] = min(jump1, jump2)
    return dp[index]


heights = [20, 30, 40, 20]
n  = len(heights)
dp = [-1] * (n)
# print(frog(n-1, dp))

"""
Time complexity : O(n)
Space complexity : O(n) + O(n)
"""

"""
3. Tabulation [Bottom - Up]
"""
heights = [20, 30, 40, 20]
n  = len(heights)
dp = [-1] * (n)

dp[0] = 0

for i in range(1, n):
    jump1 = dp[i-1] + abs(heights[i] - heights[i - 1])
    if i > 1:
        jump2 = dp[i - 2] + abs(heights[i] - heights[i -2])
    else:
        jump2 = float("inf")
    dp[i] = min(jump1, jump2)

# print(dp[n-1])

"""
Time complexity : O(n)
Space complexity : O(n)
"""

"""
4. tabulation (Space Optimation)
"""

heights = [20, 30, 40, 20]
n = len(heights)

prev2 = 0
prev = 0

for i in range(1, n):
    jump1 = prev + abs(heights[i] - heights[i-1])

    if i > 1:
        jump2 = prev2 + abs(heights[i] - heights[i-2])
    else :
        jump2 = float("inf")

    curr = min(jump1, jump2)

    prev2 = prev
    prev = curr

print(prev)

"""
Time complexity : O(n)
Space complexity : O(1)
"""