"""
120. Triangle
here start is fix and end is not fix
so do not start by reverse
start with fix
"""

def minPathSum(i, j):
    if i == 3:
        return triangle[i][j]

    down = triangle[i][j] + minPathSum(i+1, j)
    dig = triangle[i][j] + minPathSum(i+1, j+1)
    return min(dig, down)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# print(minPathSum(0,0))
"""
Time complexity : O(2 ^ n)
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""
def minPathSum(i, j, dp):
    if i == 3:
        return triangle[i][j]
    
    if dp[i][j] != -1:
        return dp[i][j]

    down = triangle[i][j] + minPathSum(i+1, j, dp)
    dig = triangle[i][j] + minPathSum(i+1, j+1, dp)
    dp[i][j] = min(dig, down)
    return dp[i][j]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
n = len(triangle) -1
dp = [[-1 for _ in range(n)] for _ in range(n)]
# print(minPathSum(0,0, dp))

"""
Time complexity : O(n x n)
Space complexity : O(n) + O(n x n)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
n = len(triangle)
dp = [[-1 for _ in range(n)] for _ in range(n)]

for j in range(n):
    dp[n-1][j] = triangle[n-1][j]

for i in range(n-2, -1, -1):
    for j in range(0, i+1):
        down = triangle[i][j] + dp[i+1][j]
        dia = triangle[i][j] + dp[i+1][j+1]

        dp[i][j] = min(down, dia)

# print(dp[0][0])

"""
Time complexity : O(n X n)
Space complexity : O(n X n)
"""

"""
4. Tabulation (Space Optimation)
"""
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
n = len(triangle)
prev = [-1] * (n)

for j in range(n):
    prev[j] = triangle[n-1][j]

for i in range(n-2, -1, -1):
    curr = [-1] * (i+1)
    for j in range(0, i+1):
        down = triangle[i][j] + prev[j]
        dia = triangle[i][j] + prev[j+1]

        curr[j] = min(down, dia)
    prev = curr

print(prev[0])

"""
Time complexity : O(n X n)
Space complexity : O(1)
"""