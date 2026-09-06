class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        tempStack = []
        curr = self.stack.pop()
        count = 1
        while self.stack and curr <= price:
            
            tempStack.append(curr)
            curr = self.stack.pop()
        while tempStack:
            item = tempStack.pop()
            self.stack.append(item)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)