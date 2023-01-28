class Solution:
    def heightChecker(self, heights: List[int]) -> int: # Runtime O(n^2); Space O(n)

        orig = [i for i in heights]

        has_swapped = True
        count = 0

        while has_swapped:
            has_swapped = False
            for i in range(len(heights) - 1):
                if heights[i] > heights[i + 1]:
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
                    has_swapped = True

        for i, j in zip(orig, heights):
            if i != j:
                count += 1
        return count

