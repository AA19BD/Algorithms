class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):  # O(n)
            d[nums[i]] = d.get(nums[i], 0) + 1

        list_ = []
        sorted_values = sorted(d.values(), reverse=True)  # O(n logn)
        s_ = sorted_values[0: k]

        # for k, v in d.items():# O(n)
        #     if v in s_:
        #         list_.append(k)
        # return list_
        return [k for k, v in d.items() if v in s_]

