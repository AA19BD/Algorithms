class Solution:#Two Pointers Technique
    def twoSum(self, numbers: list[int], target: int)-> list[int]:#O(n)
        left_p = 0
        right_p = len(numbers)-1
            
        while left_p<right_p:
            if (numbers[left_p]+numbers[right_p]==target):
                return [left_p+1,right_p+1]
            if numbers[left_p]+numbers[right_p]>target:
                right_p-=1
            if numbers[left_p]+numbers[right_p]<target:
                left_p+=1
            
        return []
    
        
        
sol=Solution()
print(sol.twoSum([2,7,11,15],9))
# # Two-Sum-II-Input-Array-Is-Sorted
