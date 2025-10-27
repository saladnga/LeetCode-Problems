class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums) + 1)
        
        MOD = 1_000_000_007
        ans = 1

        for num in nums:
            ans = (ans * num) % MOD
        return ans