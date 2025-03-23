class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = {num: 0 for num in arr}
        for num in arr:
            arr_dict[num] += 1
        arr_set = set()
        for value in arr_dict.values():
            arr_set.add(value)
        if len(arr_set) == len(arr_dict):
            return True
        else:
            return False
            