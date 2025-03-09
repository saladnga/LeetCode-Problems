class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        for i in range(n-1, -1, -1):
            if arr[i] == 0 and i != n-1:
                for j in range(n-1, i, -1):
                    if j < n-1:
                        arr[j+1] = arr[j]
                arr[i+1] = 0
