class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        path = []
        used = [False for _ in range(len(nums))]
        def backtrack() -> None:
            
            if len(path) == len(nums):
                self.results.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                used[i] = False
                path.pop()

            
        backtrack()
        return self.results
