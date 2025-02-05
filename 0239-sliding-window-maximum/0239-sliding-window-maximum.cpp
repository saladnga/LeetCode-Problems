class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> deque;
        vector<int> ans;

        for (int i = 0; i < nums.size(); i++) {
            while (deque.empty() == false && nums[i] > nums[deque.back()]) {
                deque.pop_back();
            }

            deque.push_back(i);

            if (deque.front() == i - k) {
                deque.pop_front();
            }

            if (i >= k - 1) {
                ans.push_back(nums[deque.front()]);
            }

        }
        return ans;
    }
};