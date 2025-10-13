class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ans  = 0
        for box, units in boxTypes:
            take = min(box, truckSize)
            ans += take * units
            truckSize -= take
            if truckSize == 0:
                return ans
        return ans

