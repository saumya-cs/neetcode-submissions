from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = dict()
        inDegree = dict()
        for a,b in prerequisites:
            tmp = adjList.get(b, [])
            tmp.append(a)
            adjList[b] = tmp
            inDegree[a] = inDegree.get(a, 0) + 1
        
        q = deque()
        visited = set()
        for i in range(numCourses):
            if i not in inDegree:
                q.append(i)
                visited.add(i)
        
        finishedCourses = 0
        while q:
            currentCourse = q.popleft()
            finishedCourses += 1
            if currentCourse not in adjList:
                continue
            neighbors = adjList[currentCourse]
            for neighbor in neighbors:
                inDegree[neighbor] = inDegree[neighbor] - 1
                if inDegree[neighbor] == 0 and neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return finishedCourses == numCourses


        
        