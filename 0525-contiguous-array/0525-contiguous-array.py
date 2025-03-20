class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Convert 0 to -1
        nums = [num if num == 1 else -1 for num in nums]
        # Initialize count, max_length and count_map
        count = 0
        max_length = 0
        count_map = {0: -1}
        # Traverse the array
        for i, num in enumerate(nums):
            count += num
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i
        return max_length