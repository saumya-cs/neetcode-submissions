class Solution:
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