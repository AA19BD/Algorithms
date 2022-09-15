class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l = 0  # Approach 2
            r = len(image) - 1
            while l <= r:
                i[l], i[r] = i[r], i[l]
                i[l] = 0 if i[l] else 1
                if l != r:
                    i[r] = 0 if i[r] else 1
                l += 1
                r -= 1

        return image

        # for i in range(len(image)): # Approach 1
        #     image[i] = image[i][::-1]
        #     for j in range(len(image[i])):
        #         if image[i][j] == 0:
        #             image[i][j] = 1
        #         else:
        #             image[i][j] = 0
        # return image