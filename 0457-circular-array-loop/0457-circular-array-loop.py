class Solution:
    def findNextValue(self, nums, is_forward, current_index):
        direction = nums[current_index] >= 0
        if direction != is_forward:
            return -1
        next_index = (current_index + nums[current_index]) % len(nums)
        if next_index == current_index:
            next_index = -1
        return next_index
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            slow, fast = i, i
            is_forward = nums[i] >= 0
            while True:
                slow = self.findNextValue(nums, is_forward, slow)
                fast = self.findNextValue(nums, is_forward, fast)
                if fast != -1:
                    fast = self.findNextValue(nums, is_forward, fast)
                if slow == -1 or fast == -1:
                    break
                if slow == fast:
                    return True
        return False