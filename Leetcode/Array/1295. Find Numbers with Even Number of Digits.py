class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        #         def d_num(num): # First approach

        #             res = 0

        #             while num:
        #                 num //= 10
        #                 res += 1

        #             return res

        #         count_even = 0
        #         for num in nums:
        #             if d_num(num) % 2 == 0:
        #                 count_even += 1

        #         return count_even

        count_even1 = 0  # Second approach
        for num in nums:
            if len(str(num)) % 2 == 0:
                count_even1 += 1
        return count_even1


