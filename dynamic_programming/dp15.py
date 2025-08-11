"""
minimum sum partition
"""

arr = [5,3,2]
target = sum(arr)
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
min_diff = float("inf")
for s1 in range(target + 1):
    if dp[n-1][s1] == True:
        s2 = target - s1
        min_diff = min(min_diff, abs(s1 - s2))

# print(min_diff)

"""
Time complexity : O((n x target) + (target))
Space complexity : O(n x target)
dp
"""

"""
4. Tabulation [Space optimization]
"""

arr = [5, 3, 2]
target = sum(arr)
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
# print(prev[target]) 

min_diff = float("inf")
for s1 in range(target + 1):
    if prev[s1] == True:
        s2 = target - s1
        min_diff = min(min_diff, abs(s1 - s2))

# # improved version
# min_diff = float("inf")
# for s1 in range(target // 2 + 1):
#     if prev[s1]:
#         s2 = target - s1
#         min_diff = min(min_diff, abs(s1 - s2))
print(min_diff)