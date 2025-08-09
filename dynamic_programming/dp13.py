"""

"""


def cherryPickupRec(grid, r1, c1, r2, c2):
    n = len(grid)
    
    # out of bounds or thorn
    if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
        return float("-inf")
    
    # reached bottom-right
    if r1 == n-1 and c1 == n-1:
        return grid[r1][c1]
    
    # cherries at current positions
    cherries = grid[r1][c1]
    if (r1, c1) != (r2, c2):
        cherries += grid[r2][c2]
    
    # next moves
    next_val = max(
        cherryPickupRec(grid, r1+1, c1, r2+1, c2),  # down, down
        cherryPickupRec(grid, r1, c1+1, r2, c2+1),  # right, right
        cherryPickupRec(grid, r1+1, c1, r2, c2+1),  # down, right
        cherryPickupRec(grid, r1, c1+1, r2+1, c2)   # right, down
    )
    
    cherries += next_val
    return cherries
