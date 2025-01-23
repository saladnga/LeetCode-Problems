class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        unordered_map<int, int> counts;
        for (vector<int>&arr: nums) {
            for (int x : arr) {
                counts[x]++;
            }
        }
        int n = int(nums.size());
        vector<int> ans;
        for (auto[key, val]: counts) {
            if (val == n) {
                ans.push_back(key);
            }
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};