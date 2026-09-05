class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        
    
        tempStack = [price]
        curr = None
        count = 1
        while self.stack:
            curr = self.stack.pop()
            if curr > price:
                self.stack.append(curr)
                break
            tempStack.append(curr)
            count += 1

        while tempStack:
            item = tempStack.pop()
            self.stack.append(item)
        
 
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)