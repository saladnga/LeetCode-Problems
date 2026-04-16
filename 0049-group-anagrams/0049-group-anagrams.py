class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_str = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            dict_str[key].append(word)
        return dict_str.values()
        