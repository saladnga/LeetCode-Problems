class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        total = 0
        while len(nums) != len(set(nums)):
            if len(nums) < 3:
                return total + 1
            nums = nums[3:]
            total += 1
        return total