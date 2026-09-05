import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency_map = dict()
        target = math.floor(len(nums) / 2)
        for num in nums:
            frequency_map[num] = frequency_map.get(num,0) + 1
        for k,v in frequency_map.items():
            if v > target:
                return k