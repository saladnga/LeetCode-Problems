class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum, windowStart = 0, 0
        min_len = math.inf
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            while windowSum >= target:
                curr_len = windowEnd - windowStart + 1
                min_len = min(min_len, curr_len)
                windowSum -= nums[windowStart]
                windowStart += 1
        if min_len == math.inf:
            return 0
        return min_len