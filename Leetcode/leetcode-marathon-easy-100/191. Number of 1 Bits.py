class Solution:
    def hammingWeight(self, n: int) -> int:
        # return (int(bin(n)[2:].count('1')))
        ans = 0
        while n:
            ans += (n & 1)
            n = n >> 1
        return ans