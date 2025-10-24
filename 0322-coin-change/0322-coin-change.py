class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return math.inf
            minCoin = math.inf
            for coin in coins:
                result = dp(i - coin) + 1
                minCoin = min(minCoin, result)
            return minCoin
        ans = dp(amount)
        if ans == math.inf:
            return -1
        return ans