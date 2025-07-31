"""
213. House Robber II
"""
# def backtrack(index, nums):
#     if index == 0:
#         return nums[0]
#     if index < 0:
#         return 0

#     pick = nums[index] + backtrack(index - 2, nums)
#     not_pick = backtrack(index - 1, nums)

#     return max(pick, not_pick)

# nums = [2, 3, 2]
# n = len(nums)

# if n == 1:
#     print(nums[0])
# else:
#     print(max(
#         backtrack(n - 2, nums[0:n - 1]),
#         backtrack(n - 2, nums[1:n])
#     ))


def backtrack(index, nums):
    if index == 0:
        return nums[index]
    
    if index < 0:
        return 0
    
    pick = nums[index] + backtrack(index - 2, nums)
    not_pick = 0 + backtrack(index - 1, nums)

    return max(pick, not_pick)

def rob(nums):
    if len(nums) ==1:
        return nums[0]
    ans1 = backtrack(n-2, nums[0:n-1])
    ans2 = backtrack(n-2, nums[1:n])
    return max(ans1, ans2)

nums = [2,3,2]
n = len(nums)
# print(rob(nums))

"""
Time complexity : O(2^n)
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""
def backtrack(index, nums, dp):
    if index == 0:
        return nums[index]
    
    if index < 0:
        return 0
    
    if dp[index] != -1:
        return dp[index]
    
    pick = nums[index] + backtrack(index - 2, nums, dp)
    not_pick = 0 + backtrack(index - 1, nums, dp)

    return max(pick, not_pick)

def rob(nums):
    if len(nums) ==1:
        return nums[0]
    dp = [-1] * (n)
    ans1 = backtrack(n-2, nums[0:n-1], dp)
    dp = [-1] * (n)
    ans2 = backtrack(n-2, nums[1:n], dp)
    return max(ans1, ans2)

nums = [2,3,2]
n = len(nums)
# print(rob(nums))
"""
Time complexity : O(n)
Space complexity : O(n) + O(n)
"""

"""
3. Tabulation [Bottom - Up]
"""
def solve(nums):
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
    return dp[n-1]

def rob(nums):
    if len(nums) ==1:
        return nums[0]
    ans1 = solve(nums[0:n-1])
    ans2 = solve(nums[1:n])
    return max(ans1, ans2)

nums = [2,3,2]
n = len(nums)
# print(rob(nums))

"""
Time complexity : O(n)
Space complexity : O(n)
"""

"""
4. Tabulation (Space Optimation)
"""
def solve(nums):
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
    return prev

def rob(nums):
    if len(nums) ==1:
        return nums[0]
    ans1 = solve(nums[0:n-1])
    ans2 = solve(nums[1:n])
    return max(ans1, ans2)

nums = [2,3,2]
n = len(nums)
print(rob(nums))

"""
Time complexity : O(n)
Space complexity : O(1)
"""