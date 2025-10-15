class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                num = arr[mid]
                if num >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        ans = []
        potions.sort()
        m = len(potions)
        for spell in spells:
            i = binary_search(potions, success / spell)
            ans.append(m - i)
        return ans