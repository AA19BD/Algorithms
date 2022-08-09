class MinStack:

    def __init__(self):
          self.all=[]

    def push(self, val: int) -> None:
        self.all.append(val)

    def pop(self) -> None:
        self.all.pop()

    def top(self) -> int:
        return self.all[len(self.all)-1]

    def getMin(self) -> int:
        # min=None
        # for i in self.all:
        #     if min==None:
        #         min=i
        #     if i<min:
        #         min=i
        # return min
        return min(self.all)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()