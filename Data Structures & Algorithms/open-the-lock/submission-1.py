from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        q = deque()
        if "0000" in deadends:
            return -1
        q.append(("0000", 0))
        visited = set()
        visited.add("0000")

        while q:
            curr, turn = q.popleft()
            if curr == target:
                return turn
            neighbors = []
            
           
            for i in range(4):
                #add
                tmp = int(curr[i]) + 1
                if tmp == 10:
                    tmp = 0
                neighbors.append(curr[0:i] + str(tmp) + curr[i+1:])
           

                tmp = int(curr[i]) - 1
                if tmp == -1:
                    tmp = 9
                neighbors.append(curr[0:i] + str(tmp) + curr[i+1:])

            for item in neighbors:
                if item not in dead and item not in visited:
                    visited.add(item)
                    q.append((item, turn + 1))
        return -1
