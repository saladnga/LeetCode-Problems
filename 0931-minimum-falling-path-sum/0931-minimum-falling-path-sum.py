class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            if col < 0 or col >= len(matrix[0]):
                return math.inf
            if row == 0:
                return matrix[0][col]
            ans = min(dp(row - 1, col + 1), dp(row - 1, col), dp(row - 1, col - 1))
            return matrix[row][col] + ans
        return min(dp(len(matrix) - 1, col) for col in range(len(matrix[0])))