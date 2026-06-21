class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if c in pairs.keys():
                stack.append(c)
            elif stack and c == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
