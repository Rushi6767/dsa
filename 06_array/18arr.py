"""
48. Rotate Image ,Rotate matrix 90 deegree
"""
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# r = len(matrix)
# c = len(matrix[0])

# # Properly create an empty result matrix with deep rows
# result = [[0 for _ in range(c)] for _ in range(r)]

# for i in range(r):
#     for j in range(c):
#         result[j][r - 1 - i] = matrix[i][j]

# print(result)

"""
Time complexity: O(n^2)
Space complexity: O(n^2)
"""

# optimal================

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r = len(matrix)

        for i in range(0, r-1):
            for j in range(i+1, r):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(r):
            matrix[i].reverse()
            
        return matrix
        

"""
Time complexity: O(n x n) + O(n x n) === O(n^2)
Space complexity: O(1)
"""