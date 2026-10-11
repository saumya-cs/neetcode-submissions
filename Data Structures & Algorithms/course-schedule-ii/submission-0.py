from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

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
        course_ordering = []
        finishedCourses = 0
        while q:
            currentCourse = q.popleft()
            finishedCourses += 1
            course_ordering.append(currentCourse)
            if currentCourse not in adjList:
                continue
            neighbors = adjList[currentCourse]
            for neighbor in neighbors:
                inDegree[neighbor] = inDegree[neighbor] - 1
                if inDegree[neighbor] == 0 and neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        if finishedCourses == numCourses:
            return course_ordering
        return []


        
        