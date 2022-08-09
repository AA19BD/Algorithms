class Solution:#HashMap O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         d = {}
         for i,value2 in enumerate(nums):
            #value1+value2=target
            value1 = target-value2
            if value1 in d:
                return [d[value1],i]
            else:
                d[value2]=i
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []
       