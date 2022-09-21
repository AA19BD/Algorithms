class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:  # 1 Approach
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i]:
                dp[i+1] = dp[i] + 1
            else:
                dp[i+1] = 0
        return max(dp)


class Solution(object): # 2 Approach
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans