"""
198. House Robber
"""
def backtrack(index):
    if index == 0:
        return nums[index]
    
    if index < 0:
        return 0
    
    pick = nums[index] + backtrack(index - 2)
    not_pick = 0 + backtrack(index - 1)

    return max(pick, not_pick)
    
# nums = [1,2,3,1]
nums = [2,7,9,3,1]
n = len(nums) - 1
# print(backtrack(n))

"""
Time complexity : O(2^n)
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""
def backtrack(index, dp):
    if index == 0:
        return nums[index]
        
    if index < 0:
        return 0
    
    if dp[index] != -1:
        return dp[index]
    
    pick = nums[index] + backtrack(index - 2, dp)
    not_pick = 0 + backtrack(index - 1, dp)

    dp[index] = max(pick, not_pick)
    return dp[index]
    
nums = [2,7,9,3,1]
n = len(nums)
dp = [-1] * n
# print(backtrack(n-1, dp))

"""
Time complexity : O(n)
Space complexity : O(n) + O(n)
"""

"""
3. Tabulation [Bottom - Up]
"""
nums = [2,7,9,3,1]
n = len(nums)
dp = [-1] * n

dp[0] = nums[0]

for i in range(1, n):
    if i > 1:
        pick = nums[i] + dp[i-2]
    else :
        pick = nums[i] + 0
    not_pick = 0 + dp[i-1]

    dp[i] = max(pick, not_pick)

# print(dp[n-1])
"""
Time complexity : O(n)
Space complexity : O(n)
"""

"""
4. Tabulation (Space Optimation)
"""
nums = [2,7,9,3,1]
n = len(nums)
prev2 = 0
prev = nums[0]

for i in range(1, n):
    if i > 1:
        pick = nums[i] + prev2
    else :
        pick = nums[i] + 0
    not_pick = 0 + prev

    curr = max(pick, not_pick)
    prev2 = prev
    prev = curr

print(prev)

"""
Time complexity : O(n)
Space complexity : O(1)
"""