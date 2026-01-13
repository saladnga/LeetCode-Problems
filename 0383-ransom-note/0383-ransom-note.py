class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for c in ransomNote:
            if c not in count:
                count[c] = 0
            count[c] += 1
        for c in magazine:
            if c in count:
                count[c] -= 1

        for val in count.values():
            if val > 0:
                return False  
        return True