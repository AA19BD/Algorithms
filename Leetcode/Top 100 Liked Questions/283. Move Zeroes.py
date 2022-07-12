class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[index] = nums[i]
        #         index += 1
        # for i in range(index , len(nums)):
        #     nums[i] = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1