class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def convert(n):
            if n == 0:
                return "0"
            res = ""
            while n > 0:
                res = str(n % 2) + res
                n //= 2
            return res
        return "-".join(convert(int(x)) for x in date.split("-"))