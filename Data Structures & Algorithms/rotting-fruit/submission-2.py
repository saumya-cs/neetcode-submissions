from collections import deque
class Solution:
    def bfs(self, grid, bfs_queue, total_mins):
        #while queue isn't empty
        N = len(grid)
        M = len(grid[0])
        while bfs_queue:
            row, col, minute = bfs_queue.popleft()
            
            total_mins = max(total_mins, minute)

            if row + 1 < N and grid[row+1][col] == 1:
                bfs_queue.append((row+1, col, minute + 1))
                grid[row+1][col] = 2
            if col + 1 < M and grid[row][col+1] == 1:
                bfs_queue.append((row, col + 1, minute + 1))
                grid[row][col + 1] = 2
            if col - 1 >= 0 and grid[row][col-1] == 1:
                bfs_queue.append((row, col - 1, minute + 1))
                grid[row][col - 1] = 2
            if row - 1 >= 0 and grid[row-1][col] == 1:
                bfs_queue.append((row-1, col, minute + 1))
                grid[row-1][col] = 2
            
        return total_mins
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs_queue = deque()
        total_minutes = 0
        #populate the queue with all rotten oragnes at min 0 (row,col,min)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    bfs_queue.append((r,c,0))
        total_minutes = self.bfs(grid, bfs_queue, total_minutes)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return total_minutes
        
        