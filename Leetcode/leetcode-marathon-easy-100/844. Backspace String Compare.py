class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspacing(s):
            stack = []
            for i in s:
                if i == '#':
                    if stack:
                        stack.pop()

                else:
                    stack.append(i)
            return "".join(stack)

        return backspacing(s) == backspacing(t)


