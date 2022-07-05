class MyStack:

    def __init__(self):
        self.all = []

    def push(self, x: int) -> None:
        self.all.append(x)

    def pop(self) -> int:
        return self.all.pop()

    def top(self) -> int:
        return self.all[-1]

    def empty(self) -> bool:
        return not self.all


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()