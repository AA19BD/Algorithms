class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt = 1
        ans = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev < nums[i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
            prev = nums[i]
        return ans if ans else cnt