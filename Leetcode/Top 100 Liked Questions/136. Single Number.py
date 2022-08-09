class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for k,v in d.items():
            if v==1:
                return k
#         xor = 0 [2,2,1] [4,1,2,1,2]
#         for num in nums:
#             1->xor ^= num-> xor=xor^num->1
#             2->xor ^= num-> xor=xor^num->0^4->4->4^1=5->5^2=7->7^1=6->6^2=4
        
#         return xor
# Use Xor/Bit Manipulation
# Intuition:
# Xor of any two num gives the difference of bit as 1 and same bit as 0.
# Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
# So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
# Time: O(n)
# Space: O(1)