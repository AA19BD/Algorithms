class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return 2*nums\
        # return nums+nums
        ans = []

        for i in range(0, 2 * len(nums)):
            if i < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i - len(nums)])
        return ans