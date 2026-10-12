class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(path, row, col, index):
            if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and (row,col) not in path:
                if board[row][col] == word[index]:
                    if index == len(word) - 1:
                        return True
                    path.add((row,col))
                    val = backtrack(path, row+1, col, index + 1) or backtrack(path, row-1, col, index + 1) or backtrack(path, row, col-1, index + 1) or backtrack(path, row, col+1, index + 1)
                    path.remove((row,col))
                    return val
            
        path = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if backtrack(path, r, c, 0):
                        return True
        return False


"""
 def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        self.results = []
        path = []
        def backtrack(path, index):
            if index == len(nums):
                self.results.append(path[:])
                return
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            backtrack(path, index + 1)
        backtrack(path, 0)
        return self.results
"""