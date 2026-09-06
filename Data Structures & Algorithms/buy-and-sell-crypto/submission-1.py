class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,3,6,4]
        left = 0
        right = 1
        maxProfit = 0
        while (right < len(prices) and left < len(prices) - 1):
            if prices[right] - prices[left] < 0: #no profit
                left += 1
                right += 1
            else:
                if prices[right] - prices[left] > maxProfit:
                    maxProfit = prices[right] - prices[left]
                right += 1
            if right == len(prices) - 1:
                right = left + 2
                left = left + 1
        return maxProfit


        