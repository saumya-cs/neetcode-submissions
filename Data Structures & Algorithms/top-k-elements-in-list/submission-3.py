import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = dict()
       
        for num in nums:
            freqMap[num] = freqMap.get(num,0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for key,v in freqMap.items():
            freq[v].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            lst = freq[i]
            for n in lst:
                res.append(n)
                if len(res) == k:
                    return res
           