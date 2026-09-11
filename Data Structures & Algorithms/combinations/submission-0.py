class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.results = []
        path = []
        def backtrack(start_num):
            if len(path) == k:
                self.results.append(path[:])
                return
            for i in range(start_num, n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return self.results