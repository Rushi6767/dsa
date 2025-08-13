"""
count subset with sum k
"""
def backtrack(subset, index, total):
    if total == k:
        r.append(subset.copy())
        return
    elif total > k:
        return

    if index == len(arr) :
        return
    
    total = total + arr[index]
    subset.append(arr[index])
    backtrack(subset, index + 1, total)
    e = subset.pop()
    total = total - e
    backtrack(subset, index+1, total)


# arr = [5,2,3,10,6,8]
arr = [3,2,1,0]
r = []
k = 6
backtrack([], 0, 0)
# print(r)

# ==================================================

def fun(index, total):
    if index == 0:
        if total == 0 and arr[0] == 0:
            return 2
        
        if total == 0 or arr[0] == total:
            return 1
        return 0

    if arr[index] > total:
        pick = 0
    pick = fun(index - 1, total - arr[index])
    not_pick = fun(index - 1, total)

    return pick + not_pick

arr = [3,2,1,0]
target = 6
n = len(arr)
# print(fun(n-1, target))

"""
Time complexity : O(2^n)
Space complexity : O(n)  : stack space
"""

"""
2. Memoization [Top - Down]
"""

def fun(index, total, dp):
    if index == 0:
        if total == 0 and arr[0] == 0:
            return 2
        
        if total == 0 or arr[0] == total:
            return 1
        return 0
    
    if dp[index][total] != -1:
        return dp[index][total]

    if arr[index] > total:
        pick = 0
    pick = fun(index - 1, total - arr[index], dp)
    not_pick = fun(index - 1, total, dp)

    dp[index][total] = pick + not_pick
    return dp[index][total]

arr = [3,2,1,0]
target = 6
n = len(arr)
dp = [[-1 for _ in range(target+1)] for _ in range(n)]
# print(fun(n-1, target, dp))

"""
Time complexity : O(n x target)
Space complexity : O(n) + O(n x target)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""
arr = [3,2,1,0]
target = 6
n = len(arr)
dp = [[0 for _ in range(target+1)] for _ in range(n)]

if arr[0] == 0:
    dp[0][0] = 2
else:
    dp[0][0] = 1
    if arr[0] <= target:
        dp[0][arr[0]] = 1

for index in range(1, n):
    for total in range(target + 1):
        if arr[index] > total:
            pick = 0
        pick = dp[index - 1][total - arr[index]]
        not_pick = dp[index - 1][total]

        dp[index][total] = pick + not_pick

# print(dp[n-1][target])

"""
Time complexity : O(n x target)
Space complexity : O(n x target)
dp
"""

"""
4. Tabulation [Space optimization]
"""
arr = [3,2,1,0]
target = 6
n = len(arr)
prev = [0 for _ in range(target+1)]

if arr[0] == 0:
    prev[0] = 2
else:
    prev[0] = 1
    if arr[0] <= target:
        prev[arr[0]] = 1

for index in range(1, n):
    curr = [0 for _ in range(target+1)]
    for total in range(target + 1):
        if arr[index] > total:
            pick = 0
        pick = prev[total - arr[index]]
        not_pick = prev[total]

        curr[total] = pick + not_pick

    prev = curr

print(prev[target])
"""
Time complexity : O(n x target)
Space complexity : O(2 x target) === O(1)
"""