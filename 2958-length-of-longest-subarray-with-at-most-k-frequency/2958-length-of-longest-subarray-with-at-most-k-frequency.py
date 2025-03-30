class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_length = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        return max_length