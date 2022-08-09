class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set([i for i in range(len(nums) + 1)])  # 0 1 2 3
        # return ("".join([str(i) for i in(set1.difference(nums))])) # First approach
        # return list(set(range(len(nums) + 1)) - set(nums))[0] # Second Approach

        num_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in num_set:
                return i



7