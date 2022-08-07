class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1

        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1