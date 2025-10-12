class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        for i in range(1, n + 1):
            self.heap.append(i)
        heapq.heapify(self.heap)
        

    def reserve(self) -> int:
        return heapq.heappop(self.heap)
    
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)