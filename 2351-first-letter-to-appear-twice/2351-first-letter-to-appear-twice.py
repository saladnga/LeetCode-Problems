class Solution:
    def repeatedCharacter(self, s: str) -> str:
        check = set()
        for c in s:
            if c in check:
                return c
            else:
                check.add(c)
        return " "