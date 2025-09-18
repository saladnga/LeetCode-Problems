class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window_start, window_sum = 0, 0
        freq = {}
        max_sum = 0
        # append to the freq with right most numbers
        for window_end in range(len(nums)):
            right_num = nums[window_end]
            window_sum += right_num
            if right_num not in freq:
                freq[right_num] = 0
            freq[right_num] += 1

            # if there is duplicate => shrink
            while freq[right_num] > 1:
                left_num = nums[window_start]
                freq[left_num] -= 1
                window_sum -= left_num
                window_start += 1

            # find the match length => find the new max sum and continue sliding the window
            if window_end - window_start + 1 == k:
                max_sum = max(max_sum, window_sum)
                
                left_num = nums[window_start]
                freq[left_num] -= 1
                window_sum -= left_num
                window_start += 1

        return max_sum