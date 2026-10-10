class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        returned = [0] * len(temperatures)
        for right in range(len(temperatures)-1, -1, -1):
           
            while stack and stack[-1][0] <= temperatures[right]:
                stack.pop()
            
            if stack:
                returned[right] = stack[-1][1] - right
            stack.append((temperatures[right], right))
        return returned
        