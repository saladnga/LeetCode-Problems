class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        int i = 0;
        int j = 0;
        string result;
        while (i < m || j < n) {
            if (i < m) {
                result += word1[i];
                i++;
            }
            if (j < n) {
                result += word2[j];
                j++;
            }
        }
        return result;
    }
};