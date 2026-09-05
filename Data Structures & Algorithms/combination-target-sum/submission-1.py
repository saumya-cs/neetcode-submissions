class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.results = []
        total = 0
        def backtrack(path, idx):
            nonlocal total
            if total == target:
                self.results.append(path[:])
                return
            for i in range(idx, len(nums)):
                choice = nums[i]
                path.append(choice)
                total += choice
                if (total > target):
                    num = path.pop()
                    total -= num
                    continue
                backtrack(path, i)
                num = path.pop()
                total -= num
        backtrack([], 0)
        return self.results
            