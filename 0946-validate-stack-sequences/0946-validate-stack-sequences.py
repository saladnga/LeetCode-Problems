class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        count = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[count]:
                stack.pop()
                count += 1
        return count == len(popped)