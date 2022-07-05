class Solution:
    def removeDuplicates(self, s: str) -> str:  # azxxzy
        stack = []  #
        sum_ = ""
        for i in range(len(s)):  # az
            if len(stack) != 0:
                top = stack[-1]
                if top == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])  # a

        return "".join(stack)
        # return stack