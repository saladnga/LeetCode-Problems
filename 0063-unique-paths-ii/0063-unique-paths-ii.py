class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if row < 0 or col < 0:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0 
            if row == 0 and col == 0:
                return 1
            ans = 0
            if row > 0:
                ans += dp(row - 1, col)
            if col > 0:
                ans += dp(row, col - 1)
            return ans
        return dp(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
            