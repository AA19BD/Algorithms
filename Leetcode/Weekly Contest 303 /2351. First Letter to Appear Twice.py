class Solution:
    def repeatedCharacter(self, s: str) -> str:
        h = {}
        for ch in s:
            if ch in h:
                return ch
            else:
                h[ch] = 0
        return ''