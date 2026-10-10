from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if board is None:
            return None
        num_rows = len(board)
        num_cols = len(board[0])
        # mark_safe_board = [["X" for _ in range(num_cols)] for _ in range(num_rows)]
        visited = set()
        safe_cells = set()
        q = deque()
        
        for r in range(num_rows):
            if board[r][0] == "O":
                q.append((r,0))
                visited.add((r,0))
            if board[r][num_cols - 1] == "O":
                q.append((r, num_cols - 1))
                visited.add((r,num_cols - 1))
        for c in range(num_cols):
            if board[0][c] == "O":
                q.append((0,c))
                visited.add((0,c))
            if board[num_rows - 1][c] == "O":
                q.append((num_rows - 1, c))
                visited.add((num_rows - 1, c))

        while q:
            row, col = q.popleft()
            visited.add((row, col))
            safe_cells.add((row,col))
            if row > 0 and board[row-1][col] == "O" and (row-1, col) not in visited:
                q.append((row-1,col))
            if row < num_rows - 1 and board[row+1][col] == "O" and (row+1, col) not in visited:
                q.append((row+1,col))
            if col < num_cols - 1 and board[row][col+1] == "O" and (row, col+1) not in visited:
                q.append((row,col+1))
            if col > 0 and board[row][col-1] == "O" and (row, col-1) not in visited:
                q.append((row,col-1))
        
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == "O" and (r,c) not in safe_cells:
                    board[r][c] = "X"





        
        