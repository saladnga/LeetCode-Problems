class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        for key in count:
            if count[key] == 1:
                return s.index(key)
        return -1