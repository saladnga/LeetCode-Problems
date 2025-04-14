class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        current_min = self.min_stack[0]
        for val in self.min_stack:
            if val < current_min:
                current_min = val
        return current_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()