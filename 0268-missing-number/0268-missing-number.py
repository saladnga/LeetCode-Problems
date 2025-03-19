class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for i in range(0, len(nums) + 1):
            if i not in set_nums:
                return i