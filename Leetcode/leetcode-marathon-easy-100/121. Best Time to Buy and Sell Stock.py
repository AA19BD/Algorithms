class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res_ = 0
        # max_index = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] > prices[i]:
        #             res_ = max(prices[j] - prices[i], res_)
        # return res_ if res_ else max_index

        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
