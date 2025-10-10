class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 
        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        heap = []
        for key, val in seen.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]