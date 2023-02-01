class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_left = 0
        for i in range(len(nums)):
            sum_left += nums[i]
            if sum_left == sum_nums:
                return i
            sum_nums -= nums[i]

        return -1

# 1 27
# 8 20
# 11 17
