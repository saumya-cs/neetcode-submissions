class Solution:
    def depthFirstSearch(self, row: int, col: int, grid: List[List[int]], visited_cells: set):
        #check if row,col is valid
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row,col) in visited_cells:
            return 0
        #check if row,col is land
        visited_cells.add((row,col))
        if grid[row][col] == 1:
            below = self.depthFirstSearch(row+1, col, grid, visited_cells)
            above = self.depthFirstSearch(row-1, col, grid, visited_cells)
            left = self.depthFirstSearch(row, col-1, grid, visited_cells)
            right = self.depthFirstSearch(row, col+1, grid, visited_cells)
            currArea = 1 + below + above + left + right
            return currArea
        return 0
        #if land, increment currArea

        #call dfs on neighbors

        #return currArea after updated by dfs calls

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited_cells = set()
        currMaxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in visited_cells:
                    #start a new island
                    area = self.depthFirstSearch(row, col, grid, visited_cells)
                    currMaxArea = max(area, currMaxArea)
        return currMaxArea



        