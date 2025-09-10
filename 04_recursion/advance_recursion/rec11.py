"""
Important for Hard questions
N-Queens problem
"""
class Solution:
    def isSafe1(self, row, col, board, n):
        duprow = row
        dupcol = col

        # Check upper-left diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Check left (same row)
        col = dupcol
        row = duprow
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1

        # Check lower-left diagonal
        row = duprow
        col = dupcol
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        return True

    def solve(self, col, board, ans, n):
        # Base case: all queens are placed
        if col == n:
            ans.append(list(board))
            return

        # Try placing queen in each row of the current column
        for row in range(n):
            if self.isSafe1(row, col, board, n):
                # Place queen
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                # Recur for next column
                self.solve(col + 1, board, ans, n)
                # Backtrack (remove queen)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        self.solve(0, board, ans, n)
        return ans

