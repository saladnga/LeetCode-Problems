class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopToBuses = defaultdict(list)
        queue = deque()
        usedBuses = set()
        visitedStops = set()

        if source == target:
            return 0
        
        for index, route in enumerate(routes):
            for sub_route in route:
                stopToBuses[sub_route].append(index)
        
        queue.append((source, 0))
        visitedStops.add(source)

        while queue:
            curr = queue.popleft()
            curr_stop, buses_taken = curr[0], curr[1]
            for bus in stopToBuses[curr_stop]:
                if bus in usedBuses:
                    continue
                usedBuses.add(bus)
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken + 1
                    if next_stop not in visitedStops:
                        visitedStops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
        return -1