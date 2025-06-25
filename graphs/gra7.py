"""
542. 01 Matrix (Distance to near zero)
"""
from collections import deque
from copy import deepcopy

def updateMatrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    mat_copy = deepcopy(mat)

    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    distance = [[0 for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat_copy[r][c] == 0:
                queue.append([r, c, 0])
                visited[r][c] = 1
    while queue:
        i, j, k = queue.popleft()
        distance[i][j] = k
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = i + dx, j + dy
            if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                continue

            if visited[new_i][new_j] == 1:
                continue
            queue.append([new_i, new_j, k+1])
            visited[new_i][new_j] = 1

    return distance

# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))


"""
Time complexity : O(r X c X 4) == O(r X c)
Space complexity :O(r X C X 4) == O(r X c)
"""