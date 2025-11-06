class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        first_half = word[:index + 1]
        second_half = word[index + 1:]
        first_half_reverse = first_half[::-1]
        return first_half_reverse + second_half
        