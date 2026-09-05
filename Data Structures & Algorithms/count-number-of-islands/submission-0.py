class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate through each cell in grid and run dfs on each 1 if not in set
        #use dfs on each potential island, use set to track if cell has been counted already in dfs
        
        #test cases: grid is all 0s, grid is all 1s, ex1, ex 2
        #use (row,col) to track cell
        checkedCells = set()
        numIslands = 0
        def dfs(startRow, startCol):
            if(not isValid(startRow,startCol)):
                return
            start = (startRow,startCol)
            checkedCells.add(start)
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for dir in directions:
                newRow = startRow + dir[0]
                newCol = startCol + dir[1]
                newDir = (newRow,newCol)
                if(isValid(newRow,newCol) and grid[newDir[0]][newDir[1]] == "1" and newDir not in checkedCells):
                    dfs(newDir[0],newDir[1])
            return
        def isValid(startRow,startCol):
            if(startRow < 0 or startRow >= len(grid) or startCol < 0 or startCol >= len(grid[0])):
                return False
            return True
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == "1"):
                    if ((row,col) not in checkedCells):
                        numIslands += 1
                        dfs(row,col)
        
        return numIslands
        