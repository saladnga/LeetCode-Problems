class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_val = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            val = prices[right] - prices[left]
            max_val = max(max_val, val)
        return max_val