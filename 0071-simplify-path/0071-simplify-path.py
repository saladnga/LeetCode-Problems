class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        split_path = path.split('/')
        for char in split_path:
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "/" + "/".join(stack)