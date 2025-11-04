class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        prev = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                totalTime += min(prev, neededTime[i])
                prev = max(prev, neededTime[i])
            else:
                prev = neededTime[i]
        return totalTime