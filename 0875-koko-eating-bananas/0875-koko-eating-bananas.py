class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for banana in piles:
                hours += ceil(banana / k)
            return hours <= h

        left, right = 1, max(piles)
        while left <= right:
            mid = (right + left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left