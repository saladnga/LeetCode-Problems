class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_res = max_curr = min_curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_curr, min_curr = min_curr, max_curr
            max_curr = max(nums[i], max_curr * nums[i])
            min_curr = min(nums[i], nums[i] * min_curr)
            max_res = max(max_res, max_curr)
        return max_res
