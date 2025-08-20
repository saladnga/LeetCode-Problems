class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def fix(r):
            stack = []
            for char in r:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        return fix(s) == fix(t)

        