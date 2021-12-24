from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_d = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.min_d) or (val <= self.min_d[-1]):
            self.min_d.append(val)

    def pop(self) -> None:
        popval = self.stack.pop()
        if self.min_d and (popval == self.min_d[-1]):
            self.min_d.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_d[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()