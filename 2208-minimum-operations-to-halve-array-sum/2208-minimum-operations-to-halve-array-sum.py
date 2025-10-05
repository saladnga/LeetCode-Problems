class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        ans = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while target > 0:
            ans += 1
            x = heapq.heappop(nums)
            target += x / 2
            heapq.heappush(nums, x / 2)
        return ans