from collections import deque
class MyStack:
    """
    queue1 = [3,4,5]
    queue2 = []
    """
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        oldLen = len(self.queue) #how many elems to rotate
        self.queue.append(x)
        for i in range(oldLen):
            y = self.queue.popleft()
            self.queue.append(y)

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()