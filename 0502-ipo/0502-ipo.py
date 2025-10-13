class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/709/greedy/4647/

        projects = sorted(zip(capital, profits))
        heap = []
        n = len(projects)
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            
            if len(heap) == 0:
                return w
            
            w += heapq.heappop(heap) * -1
        return w