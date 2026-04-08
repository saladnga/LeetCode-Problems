class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = [0.0 for i in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -nums[i])
            else:
                heapq.heappush(self.min_heap, nums[i])

            self.rebalance()

            if i >= k - 1:
                if len(self.max_heap) == len(self.min_heap):
                    result[i - k + 1] = (-self.max_heap[0] + self.min_heap[0]) / 2.0
                else:
                    result[i - k + 1] = -self.max_heap[0] / 1.0

                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.max_heap[0]:
                    self.remove(self.max_heap, -elementToBeRemoved)
                else:
                    self.remove(self.min_heap, elementToBeRemoved)

            self.rebalance()

        return result

    def remove(self, heap, element):
        try:
            index = heap.index(element)
            heap[index] = heap[-1]
            heap.pop()
            if index < len(heap):
                heapq._siftup(heap, index)
                heapq._siftdown(heap, 0, index)
        except ValueError:
            pass

    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        # max heap can keep 1 more element
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)