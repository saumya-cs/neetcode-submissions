class MyQueue:
    # stackA = [x]. stackB = [3,2,1]
    # queue = [3,2,1]
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, x: int) -> None:
        oldLen = len(self.stackA)
        for i in range(oldLen):
            y = self.stackA.pop()
            self.stackB.append(y)
        self.stackA.append(x)
        for i in range(oldLen):
            y = self.stackB.pop()
            self.stackA.append(y)
    def pop(self) -> int:
        return self.stackA.pop()

    def peek(self) -> int:
        return self.stackA[-1]

    def empty(self) -> bool:
        return len(self.stackA) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()