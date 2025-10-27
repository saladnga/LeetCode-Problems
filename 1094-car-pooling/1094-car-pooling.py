class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0] * (max(trip[2] for trip in trips) + 1)
        for (value, left, right) in trips:
            road[left] += value
            road[right] -= value
        curr = 0
        for i in range(len(road)):
            curr += road[i]
            if curr > capacity:
                return False
        return True