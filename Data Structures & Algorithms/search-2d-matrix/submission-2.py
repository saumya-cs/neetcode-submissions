class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while (left <= right):
            mid = (right + left) // 2
            actual_row = mid // cols
            actual_col = mid - (cols * actual_row)
            compare_val = matrix[actual_row][actual_col]
            if  compare_val == target:
                return True
            elif compare_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


        