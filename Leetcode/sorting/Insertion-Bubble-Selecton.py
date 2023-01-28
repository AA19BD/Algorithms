class Solution:
    def bubble_sort(self, lst: List[int]) -> None:
        """
        Mutates lst so that it is sorted via swapping adjacent elements until
        the entire lst is sorted.
        """
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    has_swapped = True
        return lst

    def selection_sort(self, lst: List[int]) -> None:

        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j

            lst[i], lst[min_index] = lst[min_index], lst[i]

        return lst

    def insertion_sort(self, lst: List[int]) -> None:

        for i in range(1, len(lst)):
            min_index = i

            while min_index > 0 and lst[min_index - 1] > lst[min_index]:
                lst[min_index - 1], lst[min_index] = lst[min_index], lst[min_index - 1]
                min_index -= 1
        return lst


s1 = Solution().bubble_sort([7, 3, 2, 5, 6, 10, 9, 8, 1])
s2 = Solution().selection_sort([7, 3, 2, 5, 6, 10, 9, 8, 1])
s3 = Solution().insertion_sort([7, 3, 2, 5, 6, 10, 9, 8, 1])
print(s1)
print(s2)
print(s3)
