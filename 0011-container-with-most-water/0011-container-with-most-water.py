class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea, currArea = 0, 0
        left, right = 0, len(height) - 1
        while left < right:
            shorter_height = min(height[left], height[right])
            width = right - left
            currArea = shorter_height * width
            maxArea = max(currArea, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        