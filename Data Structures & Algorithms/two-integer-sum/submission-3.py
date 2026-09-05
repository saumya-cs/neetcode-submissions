class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementToIndex = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in complementToIndex:
                return [complementToIndex[target - nums[i]],i]
            complementToIndex[nums[i]] = i


        