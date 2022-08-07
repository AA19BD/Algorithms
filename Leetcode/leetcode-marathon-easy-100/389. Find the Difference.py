class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        print(d)
        for i in t:
            if d.get(i, 0) == 0:
                return i
            else:
                d[i] -= 1