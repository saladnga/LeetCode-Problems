class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        highest = curr
        for i in gain:
            curr += i
            highest = max(highest, curr)
        return highest
            