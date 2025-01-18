class Solution {
public:
    int missingNumber(vector<int>& nums) {
       int length = nums.size();

       for (int i = 0; i < nums.size(); i++) {
        length += i - nums[i];
       } 
       return length;
    }
};