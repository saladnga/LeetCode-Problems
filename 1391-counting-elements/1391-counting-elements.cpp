class Solution {
public:
    int countElements(vector<int>& arr) {
        unordered_set<int> arr_set(arr.begin(), arr.end());
        int count = 0;
        for (int i: arr) {
            if (arr_set.count(i + 1)) {
                count++;
            }
        }
        return count;
    }
};