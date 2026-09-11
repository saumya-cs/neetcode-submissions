class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        path = []
        def backtrack(index, path):
            total = sum(path)
            if index == len(nums) and total != target:
                return
            if total > target:
                return
            if total == target:
                self.combinations.append(path[:])
                return
            #include and move on
            path.append(nums[index])
            backtrack(index, path)
            #exclude and move on
            path.pop()
            backtrack(index + 1, path)
        backtrack(0, path)
        return self.combinations
        