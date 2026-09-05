class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        def binarySearch(row):
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        for r in range(rows):
            if target == matrix[r][0] or target == matrix[r][cols-1]:
                return True
            if target >= matrix[r][0] and target <= matrix[r][cols-1]:
                return binarySearch(matrix[r])
        return False