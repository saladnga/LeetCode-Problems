class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s1) > len(s2):
            return False
        for i in range(len(s2) - k + 1):
            substring = s2[i:i+k]
            sorted_substring = sorted(substring)
            if sorted(s1) == sorted_substring:
                return True
        return False