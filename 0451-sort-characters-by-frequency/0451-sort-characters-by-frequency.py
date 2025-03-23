class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = {c: 0 for c in s}
        for c in s:
            s_dict[c] += 1
        sorted_dict = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
        result = "".join(c * count for c, count in sorted_dict)
        return result

            