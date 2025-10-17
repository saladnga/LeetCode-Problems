class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(k):
            total = 0
            for num in nums:
                total += ceil(num / k)
            return total <= threshold
        
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left