class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        max_sum = 0
        num_dict = set()
        for right in range(0, len(nums)):
            while nums[right] in num_dict:
                num_dict.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            num_dict.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        return max_sum