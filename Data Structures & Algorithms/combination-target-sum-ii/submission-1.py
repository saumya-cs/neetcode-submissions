class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        path = []
        start_vals = set()

        candidates.sort()
        def backtrack(start_index, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                self.results.append(path[:])
                return
            if start_index == len(candidates):
                return

            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, curr_sum + candidates[i])
                path.pop()
               

        backtrack(0, 0)
        return self.results