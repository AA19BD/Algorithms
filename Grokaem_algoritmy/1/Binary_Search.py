class Solution:
    def binary_search(self,nums: list[int], item) -> list[int]:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == item:
                return mid
            if nums[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
        return -1



s = Solution()
print(s.binary_search([2, 3 ,4 ,5, 8, 9, 12, 17, 21], 17))
