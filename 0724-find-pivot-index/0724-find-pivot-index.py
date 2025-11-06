class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        if n == 0:
            return - 1
        for i in range(len(nums)):
            right += nums[i]
        for i in range(len(nums)):
            right -= nums[i]
            if right == left:
                return i
            left += nums[i]
        return -1