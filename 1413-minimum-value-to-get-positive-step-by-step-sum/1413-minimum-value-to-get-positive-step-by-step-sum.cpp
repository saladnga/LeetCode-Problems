class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int minVal = 0;
        int total = 0;

        for (int num : nums){
            total += num;
            minVal = min(minVal, total);
        }

        return (-minVal) + 1;
    }
};