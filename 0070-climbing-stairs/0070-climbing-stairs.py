class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def recur_stairs(N):
            if N in cache:
                return cache[N]
            if N == 0 or N == 1:
                return 1
            else:
                result = recur_stairs(N - 1) + recur_stairs(N - 2)
            cache[N] = result
            return result
        return recur_stairs(n)