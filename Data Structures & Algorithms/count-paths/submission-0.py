class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #add from the left and from above
        grid = [[0] * n for _ in range(m)] #grid[i][j] = num of unique paths to get to that spot on grid
        grid[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                left = grid[i][j-1] if j > 0 else 0
                top = grid[i-1][j] if i > 0 else 0
                grid[i][j] =  left + top
        return grid[m-1][n-1]