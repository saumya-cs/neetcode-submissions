class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,3,6,4]
        maxProfit = 0
        minimum = prices[0]
        index = 1
        while (index < len(prices)):
            profit = prices[index] - minimum
            if profit > maxProfit:
                maxProfit = profit
            if prices[index] < minimum:
                minimum = prices[index]
            index += 1
        return maxProfit


        