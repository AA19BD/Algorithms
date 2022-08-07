class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # d = {}
        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if j != i:
        #             if (arr[i] / 2 == arr[j] or arr[i] * 2 == arr[j]) and (arr[i] in d or arr[j] in d):
        #                 return True
        #         else:
        #             d[arr[j]] = d.get(arr[j], 0) + 1
        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
            # print(seen)
        return False