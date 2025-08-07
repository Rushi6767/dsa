"""
931. Minimum Falling Path Sum

start and end are not fix
"""
def minPathSum(i, j):
    if j < 0 or j >= len(matrix[0]):
        return float("inf")
    
    if i == 0:
        return matrix[i][j]

    up = matrix[i][j] + minPathSum(i-1, j)
    dig_l = matrix[i][j] + minPathSum(i-1, j-1)
    dig_r = matrix[i][j] + minPathSum(i-1, j+1)
    return min(up, dig_l , dig_r)

def min_faling():
    r = len(matrix)
    c = len(matrix[0])
    mini = float("inf")
    for j in range(0,c):
        mini = min(mini, minPathSum(r-1, j))
    return mini


matrix = [[2,1,3],[6,5,4],[7,8,9]]
# print(min_faling())

"""
Time complexity : O(3 ^ (m X n) )
Space complexity : O(n)
"""

"""
2. Memoization [Top - Down]
"""

def minPathSum(i, j, dp):
    if j < 0 or j >= len(matrix[0]):
        return float("inf")
    
    if i == 0:
        return matrix[i][j]
    
    if dp[i][j] is not None:
        return dp[i][j]

    up = matrix[i][j] + minPathSum(i-1, j, dp)
    dig_l = matrix[i][j] + minPathSum(i-1, j-1, dp)
    dig_r = matrix[i][j] + minPathSum(i-1, j+1, dp)
    
    dp[i][j] = min(up, dig_l, dig_r)
    return dp[i][j]

def min_faling():
    r = len(matrix)
    c = len(matrix[0])
    dp = [[None for _ in range(c)] for _ in range(r)]
    mini = float("inf")
    for j in range(c):
        mini = min(mini, minPathSum(r-1, j, dp))
    return mini

matrix = [[2,1,3],[6,5,4],[7,8,9]]
# print(min_faling())

"""
Time complexity : O(n x n)
Space complexity : O(n) + O(n x n)
ss + dp
"""

"""
3. Tabulation [Bottom - Up]
"""

# def minPathSum(i, j, dp):
#     if j < 0 or j >= len(matrix[0]):
#         return float("inf")
    
#     if i == 0:
#         return matrix[i][j]
    
#     if dp[i][j] is not None:
#         return dp[i][j]

#     up = matrix[i][j] + minPathSum(i-1, j, dp)
#     dig_l = matrix[i][j] + minPathSum(i-1, j-1, dp)
#     dig_r = matrix[i][j] + minPathSum(i-1, j+1, dp)
    
#     dp[i][j] = min(up, dig_l, dig_r)
#     return dp[i][j]

def min_faling():
    r = len(matrix)
    c = len(matrix[0])
    dp = [[None for _ in range(c)] for _ in range(r)]
    for j in range(c):
        dp[0][j] = matrix[0][j]
    
    for i in range(1, r):
        for j in range(c):
            up = matrix[i][j] + dp[i-1][j]
            if j == 0:
                dig_l = float("inf")
            else:
                dig_l = matrix[i][j] + dp[i-1][j-1]

            if j == c-1:
                dig_r = float("inf")
            else:
                dig_r = matrix[i][j] + dp[i-1][j+1]

            dp[i][j] = min(up, dig_l, dig_r)

    mini = float("inf")
    for j in range(c):
        mini = min(mini, dp[r-1][j])
    return mini

matrix = [[2,1,3],[6,5,4],[7,8,9]]
# print(min_faling())
"""
Time complexity : O(n X n)
Space complexity : O(n X n)
"""

"""
4. Tabulation (Space Optimation)
"""

def min_faling():
    r = len(matrix)
    c = len(matrix[0])
    prev = [None for _ in range(c)]
    for j in range(c):
        prev[j] = matrix[0][j]
    
    for i in range(1, r):
        curr = [None] * (c)
        for j in range(c):
            up = matrix[i][j] + prev[j]
            if j == 0:
                dig_l = float("inf")
            else:
                dig_l = matrix[i][j] + prev[j-1]

            if j == c-1:
                dig_r = float("inf")
            else:
                dig_r = matrix[i][j] + prev[j+1]

            curr[j] = min(up, dig_l, dig_r)
        prev = curr

    mini = float("inf")
    for j in range(c):
        mini = min(mini, prev[j])
    return mini

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(min_faling())

"""
Time complexity : O(n X n)
Space complexity : O(1)
"""