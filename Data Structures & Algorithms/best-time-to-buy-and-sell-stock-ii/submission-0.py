class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for idx in range(1, len(prices)):
            curr = prices[idx]
            prev = prices[idx-1]
            if curr - prev > 0:
                profit += (curr - prev)
        return profit
