class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val != "." and (val in rows[r] or val in cols[c]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])

                s1,s2 = r // 3, c // 3
                if val != "." and val in squares[s1][s2]:
                    return False
                squares[s1][s2].add(board[r][c])
                # if r == N - 1:
                #     if len(cols[c]) < 9:
                #         return False
                # if c == N - 1:
                #     if len(rows[r]) < 9:
                #         return False
   
        return True