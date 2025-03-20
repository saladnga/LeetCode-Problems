class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = list(magazine)
        for c in ransomNote:
            if c in magazine_list:
                magazine_list.remove(c)
            else:
                return False
        return True