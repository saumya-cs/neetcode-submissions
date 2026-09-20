import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       
       closest = []
       for x,y in points:
            dist = abs(x) ** 2 + abs(y) ** 2
            if len(closest) < k:
                heapq.heappush(closest, (-1 * dist, x, y))
            elif len(closest) == k:
                if (-1 * dist > closest[0][0]):
                    heapq.heappush(closest,( -1 * dist, x, y))
                    heapq.heappop(closest)
       ans = []
       for i in range(len(closest)):
            ans.append([closest[i][1],closest[i][2]])
       return ans
