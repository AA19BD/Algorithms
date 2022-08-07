class Solution:
    def maximumSum(self, nums):
        def sum_of_digits(n):
            sum_ = 0
            while (n):
                sum_ += (n % 10)
                n = n // 10
            return sum_

        d = {}
        ans = -1
        pair1, pair2 = 0, 0
        for i in range(len(nums)):
            temp = sum_of_digits(nums[i])
            if (temp not in d):
                d[temp] = 0
            if (d[temp] != 0):
                if (nums[i] + d[temp] > ans):
                    pair1 = nums[i]
                    pair2 = d.get(temp)
                    ans = pair1 + pair2
            d[temp] = max(nums[i], d[temp])
        return ans
s = Solution()
print(s.maximumSum([10,12,19,14]))