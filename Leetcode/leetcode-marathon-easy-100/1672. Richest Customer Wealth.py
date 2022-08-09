class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        # # sum_ = []
        # for i in range(len(accounts)):
        #     sum = 0
        #     for j in range(len(accounts[i])):
        #         sum += accounts[i][j]
        #         # sum_.append(sum)
        #     res = max(res, sum)
        # return res

        for account in accounts:
            wealth = sum(account)
            res = max(res, wealth)
        return res