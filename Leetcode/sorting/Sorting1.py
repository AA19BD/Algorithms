class Solution:

    def sort_by_length(self, lst):
        lst.sort(key=lambda x: len(x))
        return lst


s = Solution()
print(s.sort_by_length(["hello", "world", "we", "are", "learning", "sorting"]))