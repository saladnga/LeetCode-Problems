class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check = set()
        for char in sentence:
            check.add(char)
        return len(check) == 26