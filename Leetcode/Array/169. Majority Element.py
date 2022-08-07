class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_times=len(nums)/2
        elements=dict()
        for num in nums:
            elements[num]=elements.get(num,0)+1
        for el in elements:
            if elements[el]>=count_times:
                return el