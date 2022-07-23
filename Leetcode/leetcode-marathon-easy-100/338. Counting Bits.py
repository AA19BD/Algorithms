class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [] #First method
        for i in range(n + 1):
            sum = 0
            while i:
                i, d = divmod(i, 2)
                sum += d
            ans.append(sum)
        return ans
        # Second method
        #return [bin(i)[2:].count('1') for i in range(n + 1)]
        # Third method
        # ans = []
        # for i in range(n + 1):
        #     cur = 0
        #     while i:
        #         cur += i & 1
        #         i >>= 1
        #     ans.append(cur)
        # return ans

