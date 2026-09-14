class Solution:
    def dfs(self, row, col, visited, heights):
        visited.add((row,col))
        currHeight =  heights[row][col]
        nRow = row - 1
        
        if nRow >= 0 and (nRow, col) not in visited:
            if heights[nRow][col] >= currHeight:
                self.dfs(nRow, col, visited, heights)
        nRow = row + 1
        if nRow < len(heights) and (nRow, col) not in visited:
            if heights[nRow][col] >= currHeight:
                self.dfs(nRow, col, visited, heights)
        nCol = col - 1
        if nCol >= 0 and (row, nCol) not in visited:
            if heights[row][nCol] >= currHeight:
                self.dfs(row, nCol, visited, heights)
        nCol = col + 1
        if nCol < len(heights[0]) and (row, nCol) not in visited:
            if heights[row][nCol] >= currHeight:
                self.dfs(row, nCol, visited, heights)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachesPacific = set()
        reachesAtlantic = set()
        
        #tuple of (row, col, visited)
        for c in range(len(heights[0])):
            self.dfs(0, c, reachesPacific, heights)
            self.dfs(len(heights)-1, c, reachesAtlantic, heights)
        for r in range(len(heights)):
            self.dfs(r, 0, reachesPacific, heights)
            self.dfs(r, len(heights[0]) - 1, reachesAtlantic, heights)
        return list(reachesPacific & reachesAtlantic)
        