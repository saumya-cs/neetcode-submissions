class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        ideal_sell_price = prices[len(prices)-1] 
        for i in range(len(prices)-1, -1, -1):
            maxProfit = max(maxProfit, ideal_sell_price - prices[i])
            if (prices[i] > ideal_sell_price):
                ideal_sell_price = prices[i]
        return maxProfit

        