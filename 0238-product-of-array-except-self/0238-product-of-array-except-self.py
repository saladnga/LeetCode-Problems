class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [0] * len(nums), [0] * len(nums)
        prefix_total, suffix_total = 1, 1

        for i in range(len(nums)):
            prefix[i] = prefix_total
            prefix_total *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = suffix_total
            suffix_total *= nums[i]

        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
            
        return nums