class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(row, col):
            if row == 0 and col == 0:
                return 1
            ans = 0
            if row > 0:
                ans += dp(row - 1, col)
            if col > 0:
                ans += dp(row, col - 1)
            return ans
        return dp(m - 1, n - 1)