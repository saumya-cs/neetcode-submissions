class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []
        def backtrack(path, idx):
            if sum(path) == target:
                self.results.append(path[:])
                return
            for i in range(idx, len(nums)):
                choice = nums[i]
                path.append(choice)
                if (sum(path) > target):
                    path.pop()
                    continue
                backtrack(path, i)
                path.pop()
        backtrack([], 0)
        return self.results
            