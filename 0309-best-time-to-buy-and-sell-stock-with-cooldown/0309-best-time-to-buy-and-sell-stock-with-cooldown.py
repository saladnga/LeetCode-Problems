class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, holding):
            if i >= len(prices):
                return 0
            if holding:
                ans = max(dp(i + 1, True), prices[i] + dp(i + 2, False))
            else:
                ans = max(dp(i + 1, False), -prices[i] + dp(i + 1, True))
            return ans
        return dp(0, False)