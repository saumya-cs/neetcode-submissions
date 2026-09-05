class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30, 38, 30, 36, 35, 40, 28]
        # [8, -8,  6,  -1,  5, -12, 0]
        # [1,4,1,2,1,0,0]
        
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            k = i + 1
            count = 1
            if (k == len(temperatures)):
                return result
            while (k < len(temperatures) and temperatures[k] - temperatures[i] <= 0):
                count+=1
                k+=1
            if (k < len(temperatures)):
                result[i] = count

        