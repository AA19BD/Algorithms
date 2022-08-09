class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        f, s = 0, 0
        for num in nums:
            if num == 0:
                s += 1
            else:
                f += ((s**2) + s) // 2
                s = 0
        f += ((s**2) + s) // 2
        return f
