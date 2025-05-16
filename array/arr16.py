"""
73.Set matrix zeros
"""
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# # O(n + m)
# def mark_infinity(matrix, row, col):
#     r = len(matrix)
#     c = len(matrix[0])

# # O(n)
#     for i in range(r):
#         if matrix[i][col] != 0:
#             matrix[i][col] = float("-inf")

# # O(m) 
#     for j in range(c):
#         if matrix[row][j] != 0:
#             matrix[row][j] = float("-inf")

# # O(n)
# for i in range(len(matrix)):
#     # O(m)
#     for j in range(len(matrix[i])):
#         # above total O(n x m)
#         if matrix[i][j] == 0:
#             # O(n+m)
#             mark_infinity(matrix, i, j)
            
# # O(n x m)
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == float("-inf"):
#             matrix[i][j] = 0

# print(matrix)

"""
Time complexity: O(((n + m) x (n x m)) + O(n x m))
Space complexity: O(1)
"""

# optimal solution
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
r = len(matrix)
c = len(matrix[0])

row_track = [0 for _ in range(r)]
col_track = [0 for _ in range(c)]

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 0:
            row_track[i] = -1
            col_track[j] = -1

for i in range(r):
    for j in range(c):
        if row_track[i] == -1 or col_track[j] == -1:
            matrix[i][j] = 0

print(matrix)

"""
Time complexity: O(2 x (n x m)) == O(n x m)
Space complexity: O(r + c) == O(n + m)
"""