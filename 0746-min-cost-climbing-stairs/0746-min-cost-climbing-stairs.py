class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # relation: min(cost[i - 1] + dp(i - 1), dp(i - 2), cost[i - 2]) -> min of 99 and 98
        memo = {}
        def dp(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2))
            return memo[i]

        return dp(len(cost))