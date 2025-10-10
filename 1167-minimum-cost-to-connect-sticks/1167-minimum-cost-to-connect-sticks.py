class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            first = abs(heapq.heappop(sticks))
            second = abs(heapq.heappop(sticks))
            ans += (first + second)
            heapq.heappush(sticks, first + second)
        return ans