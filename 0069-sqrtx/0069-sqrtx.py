class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        while left <= right:
            mid = (right + left) // 2
            if mid * mid <= x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans