class MinStack:

    def __init__(self):
        self.stack = []
        self.other_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.other_stack.append(val)
            return

        current_min = self.other_stack[-1]
        self.other_stack.append(min(current_min, val))
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.other_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.other_stack[-1]
