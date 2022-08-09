class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        while num:
            if num // 10 < 1:
                return num
            num, d = divmod(num, 10)
            num += d






