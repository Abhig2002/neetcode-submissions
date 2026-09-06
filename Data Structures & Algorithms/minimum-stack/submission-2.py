class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
        self.minVal = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.minVal = val
        else:
            if val < self.minVal:
                self.minVal = val

        self.stack.append(val)
        self.minimums.append(self.minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

        if self.minimums:
            self.minVal = self.minimums[-1]
        else:
            self.minVal = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]