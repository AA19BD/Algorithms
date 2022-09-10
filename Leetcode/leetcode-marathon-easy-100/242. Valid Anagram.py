class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        if d1 == d2: return True
        return False

        # return Counter(s) == Counter(t) O(n)

        # return sorted(s) == sorted(t)((n logn)