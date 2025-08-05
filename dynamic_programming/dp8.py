"""
62. Unique Paths
"""

def uniquePaths(m, n):
    if m == 0  and n == 0:
        return 1
    
    if m < 0 or n < 0:
        return 0
    
    up = uniquePaths(m-1, n)
    left = uniquePaths(m, n-1)

    return up + left


m = 3
n = 7
# print(uniquePaths(m-1, n-1))

"""
Time complexity : O(2 ^ (m X n) )
Space complexity : O(m + n)
"""

"""
2. Memoization [Top - Down]
"""
def uniquePaths(m, n, dp):
    if m == 0  and n == 0:
        return 1
    
    if m < 0 or n < 0:
        return 0
    
    if dp[m][n] != -1:
        return dp[m][n]
    
    up = uniquePaths(m-1, n, dp)
    left = uniquePaths(m, n-1, dp)

    dp[m][n] = up + left
    return dp[m][n]


m = 3
n = 7
dp = [[-1 for _ in range(n)] for _ in range(m)]
# print(uniquePaths(m-1, n-1, dp))

"""
Time complexity : O(n x m)
Space complexity : O(m + n) + O(m x n)
"""

"""
3. Tabulation [Bottom - Up]
"""
m = 3
n = 7
dp = [[-1 for _ in range(n)] for _ in range(m)]
dp[0][0] = 1

for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        if i == 0:
            up = 0
        else :
            up = dp[i -1][j]
            

        if j == 0:
            left = 0
        else:
            left = dp[i][j-1]

        dp[i][j] = up + left

# print(dp[m-1][n-1])

"""
Time complexity : O(m X n)
Space complexity : O(m X n)
"""

"""
4. Tabulation (Space Optimation)
"""

m = 3
n = 7
# prev = [-1 for _ in range(n)]
prev = [0] * (n)

for i in range(m):
    curr = [0] * (n)
    for j in range(n):
        if i == 0 and j == 0:
            curr[0] = 1
        
        else:
            if i == 0:
                up = 0
            else:
                up = prev[j]
            if j == 0:
                left = 0
            else :
                left = curr[j-1]

            curr[j] = up + left

    prev = curr.copy()
print(prev[n-1])

"""
Time complexity : O(m X n)
Space complexity : O(1)
"""