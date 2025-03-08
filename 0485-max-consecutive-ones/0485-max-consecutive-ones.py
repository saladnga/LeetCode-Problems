class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                current_count += 1
            if nums[i] == 0:
                max_count = current_count
                current_count = 0
        if max_count > current_count:
            return max_count
        else:
            return current_count