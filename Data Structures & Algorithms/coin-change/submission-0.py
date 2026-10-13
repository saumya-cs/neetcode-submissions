class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        minCoins[i] = minimum number of coins you can use to get amount i
        """
        minCoins = [float('inf')] * (amount + 1)
        minCoins[0] = 0

        for i in range(1, amount+1):
            minimum = float('inf')
            for c in coins:
                if i - c >= 0:
                    prevAmount = minCoins[i-c]
                    minimum = min(minimum, prevAmount + 1)
            minCoins[i] = minimum

        if minCoins[amount] == float('inf'):
            return -1
        else:
            return minCoins[amount]
