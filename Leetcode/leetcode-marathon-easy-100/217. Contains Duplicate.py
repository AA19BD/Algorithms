class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(nums)) == len(set(nums))
#         d = {}

#         for i in range(len(nums)):
#             d[nums[i]] = d.get(nums[i], 0) + 1

#         for i in d:
#             if d[i] >= 2:
#                 return True
#         return False

#       for i in nums:
#           if i in d:
#               return True
#           else:
#               d[i] = 1
#       return False