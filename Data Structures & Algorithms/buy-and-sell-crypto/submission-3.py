class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfitSeen = 0

        for price in prices:
            if (price < minPrice):
                minPrice = price
            maxProfitSeen = max(maxProfitSeen, price - minPrice)



        return maxProfitSeen