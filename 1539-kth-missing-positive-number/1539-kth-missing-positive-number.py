class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        arr_set = set(arr)
        curr = 1
        while True:
            if curr not in arr_set:
                missing_count += 1
                if missing_count == k:
                    return curr
            curr += 1