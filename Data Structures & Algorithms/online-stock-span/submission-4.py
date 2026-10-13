class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        tempStack = []
        count = 1
        while self.stack:
            if self.stack[-1] > price:
                break
            elem = self.stack.pop()
            tempStack.append(elem)
            count += 1
        
        while tempStack:
            self.stack.append(tempStack.pop())
        self.stack.append(price)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)