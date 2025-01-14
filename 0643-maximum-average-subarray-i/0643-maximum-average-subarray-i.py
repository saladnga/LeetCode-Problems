class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(0, k, +1):
            curr += nums[i]
        ans = curr / k
        for i in range(k, len(nums), +1):
            curr = curr + nums[i] - nums[i-k]
            ans = max(ans, curr / k)
        return ans