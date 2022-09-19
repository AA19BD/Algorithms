class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenLast = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                lenLast += 1
            elif lenLast > 0:
                break
        return lenLast
        # return len(s.split()[-1])