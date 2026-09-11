class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.results = []
        path = []
        def backtrack(start_index):
            self.results.append(path[:])
            if start_index == len(nums):
                return
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return self.results
        