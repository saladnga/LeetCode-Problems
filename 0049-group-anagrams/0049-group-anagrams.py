class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            dict_strs[key].append(word)
        return list(dict_strs.values())