class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        deque<int> increasing;
        deque<int> decreasing;
        int left = 0;
        int ans = 0;

        for (int right = 0; right < nums.size(); right++) {
            while (increasing.empty() == false && nums[right] < increasing.back()) {
                increasing.pop_back();
            }
            while (decreasing.empty() == false && nums[right] > decreasing.back()) {
                decreasing.pop_back();
            }

            increasing.push_back(nums[right]);
            decreasing.push_back(nums[right]);

            while (decreasing.front() - increasing.front() > limit) {
                if (nums[left] == increasing.front()) {
                    increasing.pop_front();
                }
                if (nums[left] == decreasing.front()) {
                    decreasing.pop_front();
                }
                left++;
            }

            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};