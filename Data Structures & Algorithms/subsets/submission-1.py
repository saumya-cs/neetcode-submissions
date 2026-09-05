class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        def recursiveHelper(path,remaining_choices):
    
            self.results.append(path[:])
            
            for i, choice in enumerate(remaining_choices):
                path.append(choice)
                recursiveHelper(path, remaining_choices[i+1:])
                path.pop()
        
        recursiveHelper([], nums)
        return self.results

        