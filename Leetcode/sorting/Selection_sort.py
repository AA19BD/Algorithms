class Solution:
    def selection_sort(self, lst): # - > O(n^2) runtime ; O(1) space
        for i in range(len(lst)):
            min_index = i
            for j in range(i+1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[min_index], lst[i] = lst[i], lst[min_index]

        return lst


s = Solution().selection_sort([7, 3, 2, 5, 6, 10, 9, 8, 1])
print(s)
