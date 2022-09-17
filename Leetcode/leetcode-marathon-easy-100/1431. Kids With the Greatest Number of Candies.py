class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # max_ = max(candies) # First Approach
        result = [False] * len(candies)
        max_ = 0
        for i in range(len(candies)):# Second Approach
            if candies[i] > max_:
                max_ = candies[i]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_:
                result[i] = True
        return result

