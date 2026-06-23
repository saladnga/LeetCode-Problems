class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_val = 0
        while left < right:
            width = right - left
            length = min(height[left], height[right])
            area = width * length
            max_val = max(max_val, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_val