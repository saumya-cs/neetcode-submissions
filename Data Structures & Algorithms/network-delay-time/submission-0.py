import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = dict()
        for ui, vi, ti in times:
            tmp = adjList.get(ui, [])
            tmp.append((ti, vi))
            adjList[ui] = tmp
        minTimes = [(0, k)]
        visited = set()
      
        maxTime = 0
        while minTimes:
            currTime, currNode = heapq.heappop(minTimes)
            if currNode in visited:
                continue
            visited.add(currNode)
            #add to time
        
            maxTime = max(currTime, maxTime)
            #end
            if len(visited) == n:
                return maxTime
            if currNode not in adjList:
                continue
            neighbors = adjList[currNode]
            for neighbor_weight, neighbor in neighbors:
                if neighbor not in visited:
                    heapq.heappush(minTimes, (currTime + neighbor_weight, neighbor))
        return -1
            


        