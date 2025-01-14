class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int ans = 0;
        long leftsection = 0;
        long total = 0;
        long rightsection = 0;

        for (int i = 0; i < nums.size(); i++) {
            total = total + nums[i];
        };

        for (int i = 0; i < nums.size() - 1; i++) {
            leftsection = leftsection + nums[i];
            rightsection = total - leftsection;
            if (leftsection >= rightsection) {
                ans = ans + 1;
            }
        }
        return ans;

    }
};