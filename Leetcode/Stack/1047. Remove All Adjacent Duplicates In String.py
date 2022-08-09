class Solution:
    def removeDuplicates(self, s: str) -> str:  # azxxzy
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
        # stack = []  #
        # sum_ = ""
        # for i in range(len(s)):  # az
        #     if len(stack) != 0:
        #         top = stack[-1]
        #         if top == s[i]:
        #             stack.pop()
        #         else:
        #             stack.append(s[i])
        #     else:
        #         stack.append(s[i])  # a
        #
        # return "".join(stack)
        # # return stack