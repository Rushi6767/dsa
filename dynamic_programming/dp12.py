"""
1463. Cherry Pickup II
"""

def maxPathSum(i, j):
    if j < 0 or j >= len(grid[0]):
        return float("-inf")
    
    if i == len(grid[0]) - 1:
        return grid[i][j]

    down = grid[i][j] + maxPathSum(i+1, j)
    dig_l = grid[i][j] + maxPathSum(i+1, j-1)
    dig_r = grid[i][j] + maxPathSum(i+1, j+1)
    return max(down, dig_l , dig_r)

def min_faling():
    r = len(grid)
    c = len(grid[0])
    r1 = maxPathSum(0,0)
    r2 = maxPathSum(0, c-1)

    return r1 + r2

grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# print(min_faling())

# overlap problem cannot be handle with above solutions

# so we run r1 and r2 together

def cherryPickup(i, j1, j2):
    if j1 < 0 or j1 >= len(grid[0]) or j2 < 0 or j2 >= len(grid[0]):
        return float("-inf")
    
    if i == len(grid) - 1:
        if j1 == j2 :
            return grid[i][j1]
        return grid[i][j1] + grid[i][j2]
    
    maxi = 0
    for new_j1 in range(-1, 2):
        for new_j2 in range(-1, 2):
            if j1 == j2:
                ans = grid[i][j1] + cherryPickup(i+1, j1+new_j1, j2+new_j2)
            else:
                ans = grid[i][j1] + grid[i][j2] + cherryPickup(i+1, j1+new_j1, j2+new_j2)
            maxi = max(maxi, ans)

    return maxi


grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
row = len(grid)
col = len(grid[0])
# print(cherryPickup(0,0,col - 1))

"""
Time complexity : O((3^n) X (3^n))
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""
def cherryPickup(i, j1, j2, dp):
    if j1 < 0 or j1 >= len(grid[0]) or j2 < 0 or j2 >= len(grid[0]):
        return float("-inf")
    
    if i == len(grid) - 1:
        if j1 == j2 :
            return grid[i][j1]
        return grid[i][j1] + grid[i][j2]
    
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    
    maxi = 0
    for new_j1 in range(-1, 2):
        for new_j2 in range(-1, 2):
            if j1 == j2:
                ans = grid[i][j1] + cherryPickup(i+1, j1+new_j1, j2+new_j2, dp)
            else:
                ans = grid[i][j1] + grid[i][j2] + cherryPickup(i+1, j1+new_j1, j2+new_j2, dp)
            maxi = max(maxi, ans)

    dp[i][j1][j2] = maxi
    return dp[i][j1][j2]


grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
row = len(grid)
col = len(grid[0])
# row x col x col
dp = [[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]
# print(cherryPickup(0,0,col - 1, dp))

"""
Time complexity : O(r X c X c)
Space complexity : O(n) + O(r X c X c)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""

grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
row = len(grid)
col = len(grid[0])
# row x col x col
dp = [[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]

for j1 in range(col):
    for j2 in range(col):
        if j1 == j2:
            dp[row-1][j1][j2] = grid[row-1][j1]
        else:
            dp[row-1][j1][j2] = grid[row-1][j1] + grid[row - 1][j2]

for i in range(row-2, -1, -1):
    for j1 in range(col):
        for j2 in range(col):
            maxi = 0
            for new_j1 in range(-1, 2):
                for new_j2 in range(-1, 2):
                    if j1 + new_j1 < 0 or j2 + new_j2 < 0 or j1 + new_j1 >= col or j2 + new_j2 >= col:
                        ans = float("-inf")
                    elif j1 == j2:
                        ans = grid[i][j1] +  dp[i+1][j1+new_j1][j2+new_j2]
                    else:
                        ans = grid[i][j1] + grid[i][j2] + dp[i+1][j1+new_j1][j2+new_j2]
                    maxi = max(maxi, ans)
            dp[i][j1][j2] = maxi

print(dp[0][0][col-1])

"""
Time complexity : O(r X c X c)
Space complexity :O(r X c X c)
dp
"""