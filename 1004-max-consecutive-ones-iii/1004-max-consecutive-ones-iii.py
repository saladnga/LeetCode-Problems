class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        curr = 0
        ans = 0
        for right in range(0, len(nums), +1):
            if nums[right] == 0:
                curr = curr + 1
            while (curr > k):
                if nums[left] == 0:
                    curr = curr - 1
                left = left + 1
            ans = max(ans, right - left + 1)
        return ans
        