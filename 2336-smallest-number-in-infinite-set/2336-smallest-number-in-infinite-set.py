class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.current = 1
        self.meet = set()
        

    def popSmallest(self) -> int:
        if self.heap:
            val = heapq.heappop(self.heap)
            self.meet.remove(val)
            return val
        val = self.current
        self.current += 1
        return val
        

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.meet:
            heapq.heappush(self.heap, num)
            self.meet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)