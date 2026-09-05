class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = dict()
        for i in range(len(nums)):
            if (nums[i] in myMap):
                return [myMap[nums[i]],i]

            myMap[target - nums[i]] = i
        return None
        