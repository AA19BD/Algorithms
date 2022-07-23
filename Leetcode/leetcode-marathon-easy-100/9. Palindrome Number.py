class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return
        new = 0
        orig = x
        while x:
            c = x % 10  # 2
            # x, d = divmod(x, 10) # 3
            new = new * 10 + c
            x //= 10
        return new == orig

        # return x == int(str(x)[::-1]) # 1