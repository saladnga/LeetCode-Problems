class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int nonZeros = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[nonZeros] = nums[i];
                nonZeros++;
            }
        }
        for (int i = nonZeros; i < nums.size(); i++) {
                nums[i] = 0;
            }
    }
};