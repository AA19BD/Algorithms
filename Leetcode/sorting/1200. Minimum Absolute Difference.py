class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_lst = sorted(arr)
        min_diff = 1e7

        for i in range(len(sorted_lst) - 1):
            min_diff = min(abs(sorted_lst[i + 1] - sorted_lst[i]), min_diff)

        lst_min_diff = []
        for i in range(len(sorted_lst) - 1):
            if abs(sorted_lst[i + 1] - sorted_lst[i]) == min_diff:
                lst_min_diff.append([sorted_lst[i], sorted_lst[i + 1]])

        return lst_min_diff

