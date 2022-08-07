class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        # d_stones = {i: index for index, i in enumerate(stones)}
        d_stones = {}

        for s in stones:
            d_stones[s] = d_stones.get(s, 0) + 1

        # print(d_stones)

        for j in jewels:
            if j in d_stones:
                cnt += d_stones.get(j, 0)

        return cnt
