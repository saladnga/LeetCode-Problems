class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        int sum = 0;

        // Edge case:
        if (n == 0) {
            return -1;
        }

        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }

        for (int i = 0; i < n; i++) {
            sum -= nums[i];
            if (left == sum) {
                return i;
            }
            left += nums[i];
        }
        return -1;
    }
};