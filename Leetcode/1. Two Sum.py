class Solution:#HashMap O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            
            seen[value] = i 
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []