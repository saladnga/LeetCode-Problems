class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(mid):
            current_sum = 0
            pieces = 0
            for s in sweetness:
                current_sum += s
                if current_sum >= mid:
                    current_sum = 0
                    pieces += 1
            return pieces >= (k + 1)
        
        left = 1
        right = sum(sweetness)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right