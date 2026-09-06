from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
            if len(freqMap) > 2:
                keys = list(freqMap.keys())
                for k,v in freqMap.items():
                    freqMap[k] -= 1
                for k in keys:
                    if freqMap[k] == 0:
                        del freqMap[k]
        return list(freqMap.keys())