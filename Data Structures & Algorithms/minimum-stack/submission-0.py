class MinStack:

    def __init__(self):
        self.items = []
        self.prev_mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.prev_mins) == 0:
            self.prev_mins.append(val)
        elif self.prev_mins[-1] >= val:
            self.prev_mins.append(val)


    def pop(self) -> None:
        a = self.items.pop()
        if a == self.prev_mins[-1]:
            self.prev_mins.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.prev_mins[-1]
        
