class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0
        i = 0
        for c in s:
            if c >= g[i]:
                count += 1
                i += 1
            if i == len(g):
                break
        return count