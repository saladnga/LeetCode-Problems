class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_dict = {num: 0 for num in nums}
        for num in nums:
            num_dict[num] += 1
        max_values = max(num_dict.values())
        total_sum = sum(value for value in num_dict.values() if value == max_values)
        return total_sum