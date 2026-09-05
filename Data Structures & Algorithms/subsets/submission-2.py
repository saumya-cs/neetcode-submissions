class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        def recursiveHelper(path,idx):
    
            self.results.append(path[:])
            
            for i in range(idx, len(nums)):
                choice = nums[i]
                path.append(choice)
                recursiveHelper(path, i + 1)
                path.pop()
        
        recursiveHelper([], 0)
        return self.results

        