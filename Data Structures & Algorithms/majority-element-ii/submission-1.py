from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            if num in freqMap or len(freqMap) < 2:
                freqMap[num] += 1
            else: 
                for k,v in freqMap.items():
                    freqMap[k] -= 1
   
                keys = list(freqMap.keys())
                for k in keys:
                    if freqMap[k] == 0:
                        del freqMap[k]
        return list(freqMap.keys())