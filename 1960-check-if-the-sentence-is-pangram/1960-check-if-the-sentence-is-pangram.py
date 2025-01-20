class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for c in sentence:
            if c not in seen:
                seen.add(c)
        return len(seen) == 26
        