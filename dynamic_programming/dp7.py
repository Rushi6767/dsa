"""
63. Unique Paths II
"""


def solve(i, j, obstacleGrid):
    if i == 0 and j == 0:
        if obstacleGrid[i][j] == 1:
            return 0
        return 1
    
    if i < 0 or j < 0:
        return 0
    
    if obstacleGrid[i][j] == 1:
        return 0
    
    up = solve(i-1, j, obstacleGrid)
    left = solve(i, j-1, obstacleGrid)

    return up + left



obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
r = len(obstacleGrid)
c = len(obstacleGrid[0])
# print(solve(r-1, c-1, obstacleGrid))

"""
2.
"""

def solve(i, j, obstacleGrid, dp):
    if i == 0 and j == 0:
        if obstacleGrid[i][j] == 1:
            return 0
        return 1
    
    if i < 0 or j < 0:
        return 0
    
    if obstacleGrid[i][j] == 1:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    up = solve(i-1, j, obstacleGrid, dp)
    left = solve(i, j-1, obstacleGrid, dp)

    dp[i][j] = up + left
    return dp[i][j]



obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
r = len(obstacleGrid)
c = len(obstacleGrid[0])
dp = [[-1 for _ in range(c)] for _ in range(r)]
# print(solve(r-1, c-1, obstacleGrid, dp))

"""
3. tabulation
"""
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
r = len(obstacleGrid)
c = len(obstacleGrid[0])
dp = [[-1 for _ in range(c)] for _ in range(r)]

if obstacleGrid[0][0] == 1:
    print(0, "stop")
dp[0][0] = 1

for i in range(r):
    for j in range(c):
        if i == 0 and j == 0:
            continue
        
        if obstacleGrid[i][j] == 1:
            dp[i][j] = 0
            continue

        if i == 0:
            up = 0
        else:
            up = dp[i-1][j]

        if j==0:
            left = 0
        else:
            left = dp[i][j-1]
        dp[i][j] = up + left
        
print(dp[r-1][c-1])

"""
4. tabulations
"""

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
r = len(obstacleGrid)
c = len(obstacleGrid[0])
prev = [-1 for _ in range(c)]

if obstacleGrid[0][0] == 1:
    print(0, "stop")
dp[0][0] = 1


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         r = len(obstacleGrid)
#         c = len(obstacleGrid[0])
#         dp = [[-1 for _ in range(c)] for _ in range(r)]

#         if obstacleGrid[0][0] == 1:
#             print(0, "stop")
#         dp[0][0] = 1

#         for i in range(r):
#             for j in range(c):
#                 if i == 0 and j == 0:
#                     continue
                
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] == 0
#                     continue

#                 if i == 0:
#                     up = 0
#                 else:
#                     up = dp[i-1][j]

#                 if j==0:
#                     left = 0
#                 else:
#                     left = dp[i][j-1]
#                 dp[i][j] = up + left
                
#         return dp[r-1][c-1]