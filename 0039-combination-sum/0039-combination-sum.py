class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(path, start, curr):
            if curr == target:
                ans.append(path.copy())
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr + num <= target:
                    path.append(num)
                    backtrack(path, i, curr + num)
                    path.pop()
        backtrack([], 0, 0)
        return ans