class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if row == 0 and col == 0:
                return grid[0][0]
            ans = math.inf
            if row > 0:
                ans = min(ans, dp(row - 1, col))
            if col > 0:
                ans = min(ans, dp(row, col - 1))
            return grid[row][col] + ans
        return dp(len(grid) - 1, len(grid[0]) - 1)