class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range (len(nums)):
            
            #I'm done, need a way to get i, I have j
                diff = target - nums[i]
                if diff in dict: 
                    return [dict[diff],i]
                dict[nums[i]] = i
