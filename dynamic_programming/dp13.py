"""
check subsequence with sum k
"""

# def backtrack(subset, index, total):
#     if total == k:
#         result.append(subset.copy())
#         return True
#     elif total > k:
#         return False
    
#     if index >= len(arr):
#         return False
    
#     subset.append(arr[index])
#     total = total + arr[index]
#     pick = backtrack(subset, index + 1, total)
#     if pick == True:
#         return True
    
#     e = subset.pop()
#     total = total - e
#     not_pick = backtrack(subset, index + 1, total)
#     return not_pick

# arr = [3,4,9]
# k = 9
# result = []
# print(backtrack([], 0, 0))

# second way

def backtrack(index, total):
    if total == 0:
        return True
    
    if index == 0:
        return arr[0] == total
        
    if arr[index] > total:
        pick = False
    else:
        pick = backtrack(index-1, total-arr[index])
    not_pick = backtrack(index-1, total)

    return pick or not_pick

arr = [5,3,2]
target = 8
n = len(arr)
# print(backtrack(n-1, target))

"""
Time complexity : O(2^n)
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""

def backtrack(index, total):
    if total == 0:
        return True
    
    if index == 0:
        return arr[0] == total
        
    if dp[index][total] != -1:
        return dp[index][total]
    
    if arr[index] > total:
        pick = False
    else:
        pick = backtrack(index-1, total-arr[index])
    not_pick = backtrack(index-1, total)

    dp[index][total] = pick or not_pick

    return dp[index][total]

arr = [5,3,2]
target = 8
n = len(arr)
dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
# print(backtrack(n-1, target))

"""
Time complexity : O(n x target)
Space complexity : O(n) + O(n x target)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""

arr = [5,3,2]
target = 8
n = len(arr)
dp = [[False for _ in range(target + 1)] for _ in range(n)]

for index in range(n):
    dp[index][0] = True

if arr[0] <= target:
    dp[0][arr[0]] = True


for index in range(1, n):
    for total in range(target+ 1):
        if arr[index] > total:
            pick = False
        else:
            pick = dp[index-1][total-arr[index]]
        not_pick = dp[index-1][total]

        dp[index][total] = pick or not_pick

# print(dp[n-1][total])

"""
Time complexity : O(n x target)
Space complexity : O(n x target)
dp
"""

"""
4. Tabulation [Space optimization]
"""
arr = [5, 3, 2]
target = 8
n = len(arr)

# prev[t] -> achievable sum t using elements up to previous index
prev = [False for _ in range(target + 1)]
prev[0] = True  # sum 0 is always achievable

# Base case for first element
if arr[0] <= target:
    prev[arr[0]] = True

# Iterate over elements
for index in range(1, n):
    curr = [False for _ in range(target + 1)]
    curr[0] = True  # sum 0 always achievable
    for t in range(1, target + 1):
        if arr[index] > t:
            pick = False
        else:
            pick = prev[t - arr[index]]
        not_pick = prev[t]
        curr[t] = pick or not_pick
    prev = curr  # move window

# Final answer
print(prev[target])  # True if subset with sum=target exists

"""
Time complexity : O(n x target)
Space complexity : O(1)
"""