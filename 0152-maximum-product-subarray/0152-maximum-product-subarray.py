class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = max(nums)
        prefix, suffix = 1, 1
        n = len(nums)
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n - 1 - i]
            ans = max(ans, prefix, suffix)
        return ans
        