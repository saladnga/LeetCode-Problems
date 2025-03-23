class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_dict = {num: 0 for num in arr}
        for num in arr:
            arr_dict[num] += 1
        lucky_nums = [num for num, count in arr_dict.items() if num == count]
        if lucky_nums:
            return max(lucky_nums)
        else:
            return -1
