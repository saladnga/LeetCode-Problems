class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(remaining, comb, next_start):
            if remaining == 0 and len(comb) == k:
                ans.append(comb.copy())
                return
            if remaining < 0 or len(comb) == k:
                return
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remaining - i - 1, comb, i + 1)
                comb.pop()
        backtrack(n, [], 0)
        return ans