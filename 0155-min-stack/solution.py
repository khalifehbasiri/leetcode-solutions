class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value) 
        elif value <= self.min_stack[-1]:
            self.min_stack.append(value) 
        else:
            return None

    def pop(self) -> None:
        if not self.min_stack:
            return None 
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()