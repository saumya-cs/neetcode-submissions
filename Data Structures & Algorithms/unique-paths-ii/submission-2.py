class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        countedPaths = [[0] * n for _ in range(m)]
        countedPaths[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    countedPaths[i][j] = 0
                    continue
                top = countedPaths[i-1][j] if i > 0 else 0
                left = countedPaths[i][j-1] if j > 0 else 0
                countedPaths[i][j] = top + left
        return countedPaths[m-1][n-1]
