class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat2 = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            row = matrix[r]
            prefixSum = row[0]
            for c in range(1, len(row)):
                self.mat2[r][c-1] = prefixSum
                prefixSum += row[c]
            self.mat2[r][len(self.mat2[r]) - 1] = prefixSum
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for r in range(row1, row2 + 1):
            if col1 == 0:
                sum += self.mat2[r][col2]
            else:
                sum += (self.mat2[r][col2] - self.mat2[r][col1-1])
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)