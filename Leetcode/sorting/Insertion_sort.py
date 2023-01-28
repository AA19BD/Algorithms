class Solution:
    def insertion_sort(self, lst):

        for i in range(1, len(lst)):
            min_index = i
            while min_index > 0 and lst[min_index-1] > lst[min_index]:
                lst[min_index - 1], lst[min_index] = lst[min_index], lst[min_index-1]
                min_index -= 1

        return lst


s = Solution().insertion_sort([7, 3, 2, 5, 6, 10, 9, 8, 1])
print(s)