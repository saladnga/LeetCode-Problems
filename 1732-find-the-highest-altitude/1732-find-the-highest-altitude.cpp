class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curr = 0;
        int highest = curr;
        for (int n : gain) {
            curr += n;
            highest = max(highest, curr);
        }
        return highest;
    }
};