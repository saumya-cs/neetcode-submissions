
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #for starts, only look at nums that don't contain i - 1 in map
        numSet = set(nums)
        
        starts = []
        for num in numSet:
            if num-1 not in numSet:
                starts.append(num)
        print(starts)
        maxLen = 1
        
        for num in starts:
            nextNum = num
            length = 0
            while (nextNum in numSet):
                length += 1
                nextNum += 1
            maxLen = max(maxLen, length)
        return maxLen
                
        