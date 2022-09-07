class Solution1:
    def find_even(self, w: int) -> int:
        check = False
        for i in range(2, w + 1, 2): # 2 4 6 8
            for j in range(2, w + 1, 2):
                if i + j == w:
                    check = True
        return check


s = Solution1()
w = int(input())
if s.find_even(w):
    print('YES')
else:
    print('NO')
import math

# class Solution2:
#     def find_even(self, w: int) -> int:
#        for i in range(2, math.floor(math.sqrt(w)+1)):
#            if w % i != 0:
#                return True
#        return False
#
# s = Solution2()
# w = int(input())
# if w % 2 != 0 or s.find_even(w):
#     print('NO')
# else:
#     print('YES')