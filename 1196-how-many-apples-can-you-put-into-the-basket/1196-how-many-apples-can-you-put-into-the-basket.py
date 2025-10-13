class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight = sorted(weight)
        ans = 0
        threshold = 5000
        for w in weight:
            if w <= threshold:
                ans += 1
                threshold -= w
        return ans