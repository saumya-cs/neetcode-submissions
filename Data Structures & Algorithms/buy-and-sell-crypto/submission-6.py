class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPreviousPrice = prices[0]
        maxProfit = 0
        for p in range(len(prices)):

            minPreviousPrice = min(minPreviousPrice,prices[p])
            maxProfit = max(maxProfit, prices[p] - minPreviousPrice)
        return maxProfit
