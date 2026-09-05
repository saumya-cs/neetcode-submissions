class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        table = [0] * (n+2) #table[i] = minCost to reach top from index i
        table[n] = 0
        table[n+1] = 0

        for i in range(n-1, -1, -1):
            table[i] = cost[i] + min(table[i+1], table[i+2])
        return min(table[0],table[1])
         