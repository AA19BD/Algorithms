class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in strs:
            sorted_ = "".join(sorted(i))
            if sorted_ not in h:
                h[sorted_] = [i]
            else:
                h[sorted_].append(i)
        list_ = []
        for i in h:
            list_.append(h[i])
        return list_