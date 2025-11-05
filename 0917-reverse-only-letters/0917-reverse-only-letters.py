class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        words = [word for word in s if word.isalpha()]
        words = words[::-1]
        result = []
        for c in s:
            if c.isalpha():
                result.append(words.pop(0))
            else:
                result.append(c)
        return "".join(result)