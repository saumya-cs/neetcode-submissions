from collections import deque
class Solution:
    def addValidNeighbors(self, grid, row, col, N, M, queue, depth, INF):
        if row + 1 < N and grid[row + 1][col] == INF:
            queue.append((row+1, col, depth))
        if row - 1 >= 0 and grid[row - 1][col] == INF:
            queue.append((row-1, col, depth))
        if col + 1 < M and grid[row][col + 1] == INF:
            queue.append((row, col + 1, depth))
        if col - 1 >= 0 and grid[row][col - 1] == INF:
            queue.append((row, col - 1, depth))

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        bfs_queue = deque()
        N, M = len(grid), len(grid[0])
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    bfs_queue.append((r,c,0))
        self.bfs(grid, bfs_queue, INF)
        
    def bfs(self, grid, bfs_queue, INF):
        N, M = len(grid), len(grid[0])
        while bfs_queue:
            curr_row, curr_col, curr_depth = bfs_queue.popleft()
            value = grid[curr_row][curr_col]
            if value == 0: #treasure
                self.addValidNeighbors(grid, curr_row, curr_col, N, M, bfs_queue, 1, INF)
            elif value == -1:
                continue
            else: #land
                if value == INF:
                    grid[curr_row][curr_col] = curr_depth
                    self.addValidNeighbors(grid, curr_row, curr_col, N, M, bfs_queue, curr_depth + 1, INF)
                
                
                
        

        