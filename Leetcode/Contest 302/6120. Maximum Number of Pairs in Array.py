class Solution:
    def numberOfPairs(self, nums):
        if len(nums) == 1:
            return [0, 1]
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        count1 = 0
        count2 = 0
        for k, v in d.items():
            count1 += v // 2
            count2 += v % 2
        return [count1, count2]


s = Solution()
print(s.numberOfPairs([0]))
