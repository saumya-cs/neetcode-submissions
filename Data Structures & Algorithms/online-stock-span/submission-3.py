class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        curr = (price, 1)
        span = 0
        while self.stack and self.stack[-1][0] <= price:
            curr = self.stack.pop()
            span += curr[1]
    
        self.stack.append((price, span + 1))
        return span + 1



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)