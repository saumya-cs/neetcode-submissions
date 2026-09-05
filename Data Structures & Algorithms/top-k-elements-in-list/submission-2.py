import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict()
        heap = []
        for num in nums:
            freqs[num] = freqs.get(num,0) + 1

        for num in freqs:
            tup = (freqs[num], num)
            if len(heap) < k:
                heapq.heappush(heap, tup)
            else:
                if tup[0] > heap[0][0]:
                    heapq.heappushpop(heap, tup)
        
        res = []
        for freq, val in heap:
            res.append(val)
        return res