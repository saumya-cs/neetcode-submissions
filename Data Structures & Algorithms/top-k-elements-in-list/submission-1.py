import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict()
        for num in nums:
            freqs[num] = freqs.get(num,0) + 1
        topKElems = []
        for num,freq in freqs.items():
            if (len(topKElems) < k):
                heapq.heappush(topKElems, (freq,num))
            elif (topKElems[0][0] < freq):
                heapq.heappop(topKElems)
                heapq.heappush(topKElems, (freq,num))
        returned = []
        while (topKElems):
            returned.append(topKElems[0][1])
            heapq.heappop(topKElems)
        return returned
        