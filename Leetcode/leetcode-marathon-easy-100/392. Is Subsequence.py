class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s)[::-1]  # cba
        # print(stack)

        for c in t:
            if stack and stack[-1] == c:
                stack.pop()
        return not stack
