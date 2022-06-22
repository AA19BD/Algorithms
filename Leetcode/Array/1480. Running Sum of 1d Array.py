class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sum_ = 0
        for i in range(len(nums)):
            sum_ = 0
            for j in range(0, i + 1):
                sum_ += nums[j]
            running_sum.append(sum_)

        return running_sum

    # for i in range(1, len(nums)):
    #     nums[i] = nums[i - 1] + nums[i]
    #
    # return nums