class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        max_val = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_val = max(max_val, prices[right] - prices[left])   
            else:
                left = right
            right += 1
        return max_val