class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        curr = 1
        windowStart = 0
        total, result = 0, 0
        for windowEnd in range(len(nums)):
            result += nums[windowEnd]
            while result * (windowEnd - windowStart + 1) >= k:
                result -= nums[windowStart]
                windowStart += 1
            total += windowEnd - windowStart + 1
        return total 