"""
64. Minimum Path Sum
"""
def minPathSum(i, j):
    if i == 0 and j == 0:
        return grid[0][0]
    
    if i < 0 or j < 0:
        return float("inf")

    up = minPathSum(i-1, j)
    left = minPathSum(i, j-1)
    return grid[i][j] + min(left, up)


grid = [[1,3,1],[1,5,1],[4,2,1]]
# print(minPathSum(2,2))

"""
Time complexity : O(2 ^ (m X n) )
Space complexity : O(m + n)
"""

"""
2. Memoization [Top - Down]
"""
def minPathSum(i, j, dp):
    if i == 0 and j == 0:
        return grid[0][0]
    
    if i < 0 or j < 0:
        return float("inf")
    
    if dp[i][j] != -1:
        return dp[i][j]

    up = minPathSum(i-1, j, dp)
    left = minPathSum(i, j-1, dp)
    dp[i][j] = grid[i][j] + min(left, up)
    return dp[i][j]


grid = [[1,3,1],[1,5,1],[4,2,1]]
r = len(grid)
c = len(grid[0])
dp = [[-1 for _ in range(c)] for _ in range(r)]
# print(minPathSum(2,2, dp))

"""
Time complexity : O(n x m)
Space complexity : O(m + n) + O(m x n)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""
grid = [[1,3,1],[1,5,1],[4,2,1]]
r = len(grid)
c = len(grid[0])
dp = [[-1 for _ in range(c)] for _ in range(r)]
dp[0][0] = grid[0][0]

for i in range(r):
    for j in range(c):
        if i == 0 and j == 0:
            continue

        if i == 0:
            up = float("inf")
        else :
            up = dp[i -1][j]

        if j == 0:
            left = float("inf")
        else:
            left = dp[i][j-1]

        dp[i][j] = grid[i][j] + min(up, left)

# print(dp[2][2])

"""
Time complexity : O(m X n)
Space complexity : O(m X n)
"""

"""
4. Tabulation (Space Optimation)
"""
grid = [[1,3,1],[1,5,1],[4,2,1]]
r = len(grid)
c = len(grid[0])
prev = [0] * (c)

for i in range(r):
    curr = [0] * (c)
    for j in range(c):
        if i == 0 and j == 0:
            curr[0] = grid[0][0]
            continue
        else:
            if i == 0:
                up = float("inf")
            else :
                up = prev[j]

            if j == 0:
                left = float("inf")
            else:
                left = curr[j-1]

            curr[j] = grid[i][j] + min(up, left)
    prev = curr.copy()

print(prev[2])

"""
Time complexity : O(m X n)
Space complexity : O(1)
"""