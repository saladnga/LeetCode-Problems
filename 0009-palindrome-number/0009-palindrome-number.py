class Solution:
    def isPalindrome(self, x: int) -> bool:
        result1 = []
        result2 = []
        x_str = str(x)
        for i in range(len(x_str)):
            result1.append(x_str[i])
        for j in range(len(x_str) - 1, -1, -1):
            result2.append(x_str[j])
        if "".join(result1) == "".join(result2):
            return True
        return False