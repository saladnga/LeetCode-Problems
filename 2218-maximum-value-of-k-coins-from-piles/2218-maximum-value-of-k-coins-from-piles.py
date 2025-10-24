class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(i, remain):
            if i == len(piles):
                return 0
            ans = dp(i + 1, remain)
            curr = 0
            for j in range(min(remain, len(piles[i]))):
                curr += piles[i][j]
                ans = max(ans, curr + dp(i + 1, remain - j - 1))
            return ans
        return dp(0, k)