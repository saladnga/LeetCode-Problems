class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_count = 0;
        int current_count = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                current_count++;
            }
            if (nums[i] == 0) {
                max_count = max(max_count, current_count);
                current_count = 0;
            }
        }
        return max(max_count, current_count);
    }
};