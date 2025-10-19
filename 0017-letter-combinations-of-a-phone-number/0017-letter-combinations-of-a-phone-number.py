class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapped = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                ans.append("".join(currStr.copy()))
                return 
            for letter in mapped[digits[i]]:
                currStr.append(letter)
                backtrack(i + 1, currStr)
                currStr.pop()
        backtrack(0, [])
        return ans
            