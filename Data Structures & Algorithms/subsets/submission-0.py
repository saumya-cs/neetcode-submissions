class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #for each number, decide to skip or include it 
        result = []
        def recursiveHelper(listSoFar, currIndex):
            if(currIndex >= len(nums)):
                result.append(listSoFar[:])
                return 
            recursiveHelper(listSoFar, currIndex + 1)
            listSoFar.append(nums[currIndex])
            recursiveHelper(listSoFar,currIndex + 1)
            listSoFar.pop()
        recursiveHelper([], 0)
        return result
