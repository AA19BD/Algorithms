class Solution:
    def selection_sort(self, arr: list[int]) -> list[int]: # Time Complexity(O(n^2)) # Space Complexity (O(1))
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j


            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr #[11, 12, 22, 25, 64]







s = Solution()
print(s.selection_sort([64, 25, 12, 22, 11]))