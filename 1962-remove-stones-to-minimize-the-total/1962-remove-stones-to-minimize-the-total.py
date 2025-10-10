class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k > 0:
            res = -heapq.heappop(piles)
            res_floor = floor(res / 2)
            heapq.heappush(piles, -(res - res_floor))
            k -= 1
        return -sum(piles)