class Solution {
public:
    bool backspaceCompare(string s, string t) { 
        return buildString(s) == buildString(t);
    }
    string buildString(string s) {
        string ans = "";
        for (char c : s) {
            if (c != '#') {
                ans.push_back(c);
            }
            else if (ans.empty() == false) {
                ans.pop_back();
            }
        }
        return ans;
    }
};