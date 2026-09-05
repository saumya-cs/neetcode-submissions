class Solution:
    def climbStairs(self, n: int) -> int:
        #either climb 1 or climb 2 -> those are 2 options
         #table[i] = number of ways to reach step i
        if n == 1: return 1
        if n == 2: return 2
        table = [0] * (n+1) #so indices match step numbers
        table[1] = 1
        table[2] = 2
        for i in range(3, n+1):
            table[i] = table[i-1] + table[i-2]
        return table[n]