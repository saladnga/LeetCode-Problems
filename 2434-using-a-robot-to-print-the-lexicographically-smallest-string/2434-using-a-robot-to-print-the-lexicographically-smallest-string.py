class Solution:
    def robotWithString(self, s: str) -> str:
        t, result = [], []
        n = len(s)
        min_suffix = [""] * n
        min_suffix[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        for i in range(n):
            t.append(s[i])
            # Pop từ stack nếu an toàn (nhỏ hơn hoặc bằng ký tự nhỏ nhất còn lại)
            while t and (i == n - 1 or t[-1] <= min_suffix[i + 1]):
                result.append(t.pop())
        return "".join(result)
        
