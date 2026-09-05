from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            if num in freqMap or len(freqMap) < 2:
                freqMap[num] += 1
            else: 
                keys = list(freqMap.keys())
                for k in keys:
                    freqMap[k] -= 1
                    if freqMap[k] == 0:
                        del freqMap[k]
   
                
               
        return [cand for cand in freqMap if nums.count(cand) > len(nums) // 3]

