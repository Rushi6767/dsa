"""
0 - 1 Knapsack Problem
"""

def backtrack(index, w):
    if index == 0:
        if wt[index] <= w:
            return val[index]
        return 0

    if wt[index] > w:
        pick = float("-inf")
    else:
        pick = val[index] + backtrack(index-1, w-wt[index])

    not_pick = 0 + backtrack(index - 1, w)

    return max(pick, not_pick)


wt =  [5, 4, 2, 3]
val = [10, 40, 30, 50]
w = 5
n = len(wt)
# print(backtrack(n-1,w))

"""
Time complexity : O(2^n)
Space complexity : O(n)  : stack space
"""

"""
2. Memoization [Top - Down]
"""
def backtrack(index, w,dp):
    if index == 0:
        if wt[index] <= w:
            return val[index]
        return 0
    
    if dp[index][w] != -1:
        return dp[index][w]

    if wt[index] > w:
        pick = float("-inf")
    else:
        pick = val[index] + backtrack(index-1, w-wt[index], dp)

    not_pick = 0 + backtrack(index - 1, w, dp)

    dp[index][w] = max(pick, not_pick)
    return dp[index][w]


wt =  [5, 4, 2, 3]
val = [10, 40, 30, 50]
w = 5
n = len(wt)
dp = [[-1 for _ in range(w+1)] for _ in range(n)]
# print(backtrack(n-1,w, dp))

"""
Time complexity : O(n x w)
Space complexity : O(n) + O(n x w)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""
wt =  [5, 4, 2, 3]
val = [10, 40, 30, 50]
w = 5
n = len(wt)
dp = [[0 for _ in range(w+1)] for _ in range(n)]

for w0 in range(w+1):
    if wt[0] <= w0:
        dp[0][w0] = val[0]

for index in range(1,n):
     for w in range(w+1):
        if wt[index] > w:
                pick = float("-inf")
        else:
            pick = val[index] + dp[index-1][w-wt[index]]

        not_pick = 0 + dp[index-1][w]

        dp[index][w] = max(pick, not_pick)

# print(dp[n-1][w])

"""
Time complexity : O(n x w)
Space complexity : O(n x w)
dp
"""

"""
4. Tabulation [Space optimization]
"""

wt =  [5, 4, 2, 3]
val = [10, 40, 30, 50]
w = 5
n = len(wt)
prev = [0 for _ in range(w+1)]

for w0 in range(w+1):
    if wt[0] <= w0:
        prev[w0] = val[0]

for index in range(1,n):
    curr = [0 for _ in range(w+1)]
    for w in range(w+1):
        if wt[index] > w:
                pick = float("-inf")
        else:
            pick = val[index] + prev[w-wt[index]]

        not_pick = 0 + prev[w]

        curr[w] = max(pick, not_pick)
    prev = curr

# print(prev[w])

"""
Time complexity : O(n x w)
Space complexity : O(prev + curr) == O(2w)
"""

wt =  [5, 4, 2, 3]
val = [10, 40, 30, 50]
w = 5
n = len(wt)
prev = [0 for _ in range(w+1)]

for w0 in range(w+1):
    if wt[0] <= w0:
        prev[w0] = val[0]

for index in range(1, n):
    for cap in range(w, -1, -1):  # renamed w -> cap
        if wt[index] > cap:
            pick = 0  # or float("-inf"), but 0 is simpler
        else:
            pick = val[index] + prev[cap - wt[index]]
        not_pick = prev[cap]
        prev[cap] = max(pick, not_pick)

print(prev[w])  # now works correctly


"""
Time complexity : O(n x w)
Space complexity : O(prev) == O(w)
dp
"""