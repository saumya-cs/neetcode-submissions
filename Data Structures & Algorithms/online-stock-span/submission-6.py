class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        
        curr = [price, 1]
        while self.stack and price >= self.stack[-1][0]:
            curr[1] += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append((curr[0], curr[1]))
        return curr[1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)