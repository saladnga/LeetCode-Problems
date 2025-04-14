class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dir = deque()
        n = len(senate)
        result1 = "Dire"
        result2 = "Radiant"
        for i in range(n):
            if senate[i] == "R":
                rad.append(i)
            else:
                dir.append(i)
        while rad and dir:
            if rad[0] < dir[0]:
                n += 1
                rad.append(n)
            else:
                n += 1
                dir.append(n)
            rad.popleft()
            dir.popleft()
        if not rad:
            return result1
        else:
            return result2

        