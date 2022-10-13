class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = []
        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                ans.append(nums[r] ** 2)
                r -= 1

            else:
                ans.append(nums[l] ** 2)
                l += 1
        return ans[::-1]

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [None for _ in A]
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[index] = A[left] ** 2
                left += 1
            else:
                result[index] = A[right] ** 2
                right -= 1
        return result