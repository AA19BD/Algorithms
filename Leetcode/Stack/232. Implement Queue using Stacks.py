class MyQueue:

    def __init__(self):
         self.all=[]

    def push(self, x: int) -> None:
         self.all.append(x)

    def pop(self) -> int:
        return self.all.pop(0)

    def peek(self) -> int:
        return self.all[0]

    def empty(self) -> bool:
        return not (self.all)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()