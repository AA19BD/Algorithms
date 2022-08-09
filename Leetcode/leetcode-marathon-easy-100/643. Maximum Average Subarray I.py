class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = float('-inf')
        cur = 0
        cnt = 0
        for num in range(len(nums)):
            cur += nums[num]
            cnt += 1
            if cnt == k:
                ans = max(ans, cur / k)
            if cnt > k:
                cur -= nums[num - k]
                ans = max(ans, cur / k)

        return ans


