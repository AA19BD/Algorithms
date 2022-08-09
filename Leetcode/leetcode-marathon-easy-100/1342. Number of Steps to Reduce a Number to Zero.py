class Solution:
    def numberOfSteps(self, num: int) -> int:  # 2
        s = bin(num)[2:]  # '0b10' -> '10'
        return s.count('1') + len(s) - 1  # 1 + 1 = 2 steps
#         if num == 0:
#             return 0

#         steps = 0
#         while num:
#             if num % 2 == 0:
#                 num //= 2
#                 steps += 1
#             else:
#                 num -= 1
#                 steps += 1

#         return steps

