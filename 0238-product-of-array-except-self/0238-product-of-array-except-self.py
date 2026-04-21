class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        prefix, suffix = 1, 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res