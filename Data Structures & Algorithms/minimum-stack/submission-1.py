class MinStack:
  #store the minimum of mainStack[0..i] at minimumStack[i]

    def __init__(self):
        self.length = 0
        self.mainStack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if (self.length == 0):
            self.minimumStack.append(val)
        elif(val < self.minimumStack[-1]):
            self.minimumStack.append(val)
        else:
            self.minimumStack.append(self.minimumStack[-1])
        self.length += 1


    def pop(self) -> None:
        self.mainStack.pop()
        self.minimumStack.pop()
        if (self.mainStack):
            self.length -= 1

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
