class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                previous_char = stack[-1]
                if matching.get(previous_char) != c:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0