from collections import deque
import numpy as np
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        currRow = 0
        currCol = 0
        q = deque()
        visited = set()
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    currRow, currCol = r,c
                    q.append((currRow, currCol))
                    visited.add((currRow, currCol))
                    break
        while q:
            currRow, currCol = q.popleft()
            curr = np.array([currRow, currCol])
            neighbors = [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]
            def outOfBounds(arr):
                row = arr[0]
                col = arr[1]
                if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
                    return True
                return False
            for arr in neighbors:
                neighbor = curr + arr
                if outOfBounds(neighbor) or grid[neighbor[0]][neighbor[1]] == 0:
                    perimeter += 1
                else:
                    if (neighbor[0], neighbor[1]) not in visited:
                        q.append((neighbor[0], neighbor[1]))
                        visited.add((neighbor[0], neighbor[1]))
        return perimeter
            



        