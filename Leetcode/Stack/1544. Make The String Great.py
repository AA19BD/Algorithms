class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  #
        sum_ = ""
        for i in range(len(s)):  # az
            if len(stack) != 0:
                top = stack[-1]
                if ord(top) == ord(s[i]) + 32 or ord(top) == ord(s[i]) - 32 :
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])  # a

        return "".join(stack)