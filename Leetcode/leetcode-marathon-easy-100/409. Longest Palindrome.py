class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for l, c in cnt.items():
            cur = c - (c % 2) # 0 0 4 2
            ans += cur # 0 0 4 2 => 6
            cnt[l] -= cur # a:1 b:1 c:0 d:0
        return ans if not sum(cnt.values()) else ans + 1