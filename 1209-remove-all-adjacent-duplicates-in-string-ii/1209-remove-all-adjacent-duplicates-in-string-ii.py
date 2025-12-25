class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        for (c, k) in stack:
            while k > 0:
                res.append(c)
                k -= 1
        return "".join(res)